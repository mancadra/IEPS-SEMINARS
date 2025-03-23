from urllib.parse import urlsplit, urlunsplit, urlencode, parse_qsl
import requests
from bs4 import BeautifulSoup
import heapq
from db_handler import DbHandler
import hashlib
from datetime import datetime
from helper import Helper
from min_hash import MinHasher
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

hasher = MinHasher(shingle_size=3, hash_number=250)
helper = Helper()
config = helper.get_config()
site_id = None
current_page_id = None

db_handler = DbHandler()

class PreferentialWebCrawler:
    def __init__(self, seed_url, keyword, max_pages=10):
        self.seed_url = seed_url
        self.keyword = keyword
        self.max_pages = max_pages
        url_parts = urlsplit(seed_url)
        self.domain = url_parts.scheme + "://" + url_parts.netloc
        self.visited = set()
        self.queue = []  # Priority queue (min-heap)
        heapq.heappush(self.queue, (0, seed_url, 0))  # Start with the seed URL (highest priority)

    def normalize_url(self, url):
        """Normalize URLs by removing trailing slashes, lowercasing, and sorting query parameters."""
        parsed = urlsplit(url)
        normalized_path = parsed.path.rstrip("/")  # Remove trailing slash
        normalized_netloc = parsed.netloc.lower()  # Convert to lowercase
        sorted_query = urlencode(sorted(parse_qsl(parsed.query)))  # Sort query params

        return urlunsplit((parsed.scheme, normalized_netloc, normalized_path, sorted_query, ""))

    def get_canonical_url(self, html, url):
        """Extracts the canonical URL from the page, or returns the original URL if no canonical link exists."""
        soup = BeautifulSoup(html, "html.parser")
        canonical_link = soup.find("link", rel="canonical")

        if canonical_link and canonical_link.get("href"):
            canonical_url = canonical_link["href"]

            # Ensure absolute URL
            if canonical_url.startswith("/"):
                parsed_url = urlsplit(url)
                canonical_url = f"{parsed_url.scheme}://{parsed_url.netloc}{canonical_url}"

            #return self.normalize_url(canonical_url)
            canonical_url = self.normalize_url(canonical_url)
            print(f"Extracted canonical URL: {canonical_url} (Original: {url})")
            return canonical_url

        print(f"No canonical URL found. Using original: {url}")
        return self.normalize_url(url)

    def fetch_page(self, url):
        """Fetch page content from a URL."""
        try:
            response = requests.get(url, timeout=5)
            response.encoding = 'utf-8'
            if response.status_code == 200:
                accessed_time = datetime.now()
                page_type_code = self.get_page_type(response.headers['Content-Type'])
                return response.text, response.status_code, accessed_time, page_type_code
        except requests.RequestException as e:
            helper.log_error(e)
        return None

    def get_page_type(self, mime_page_type):
        if 'text/html' in mime_page_type:
            return 'HTML'
        elif "application" in mime_page_type:
            return 'BINARY'
        else:
            return 'UNKNOWN'

    def extract_links(self, html, base_url):
        """Extract and return all links from the HTML content."""
        soup = BeautifulSoup(html, "html.parser")
        links = []
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            if href.startswith("http"):
                links.append((href, a_tag))
            elif href.startswith("//"):
                links.append(("https:" + href, a_tag))
            elif href.startswith("/"):
                links.append((base_url + href, a_tag))
        return links

    def in_domain(self, url):
        return url.startswith(self.domain)

    def priority(self, html, link, link_tag):
        """
        Compute the priority of a link.

        Args:
            html (str): HTML content of the page.
            link (str): Link URL.
            link_tag (bs4.Tag): BeautifulSoup tag representing the link.

        Returns:
            float: Priority score (lower number represents high priority).
        """
        priority = 0 if self.keyword in link else 1  # Assign priority (0 = high, 1 = lower)
        return priority

    def extract_image_urls_with_selenium(self, url):
        """
        Extract image URLs using Selenium.
        """

        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        driver = webdriver.Chrome(options=chrome_options)

        try:
            driver.get(url)

            # Wait for the page to fully load
            time.sleep(5)  # Wait for JavaScript to render the content

            # Locate the <div id="fotografije"> element
            try:
                fotografije_div = driver.find_element(By.ID, "fotografije")
            except NoSuchElementException:
                print("No <div id='fotografije'> found. Skipping this page.")
                return []

            # Find all <img> tags within the <div id="fotografije">
            images = fotografije_div.find_elements(By.TAG_NAME, "img")

            image_urls = []
            for img in images:
                # Try to get the URL from the `data-default` attribute first
                data_default = img.get_attribute("data-default")

                if data_default is not None and data_default.endswith(".webp"):
                    image_urls.append(data_default)
                else:
                    # Fallback to `data-srcset` if `data-default` is not available
                    data_srcset = img.get_attribute("data-srcset")

                    if data_srcset:
                        # Extract the highest resolution URL from `data-srcset`
                        srcset_urls = data_srcset.split(", ")
                        for url in srcset_urls:
                            if url.strip().endswith(".webp") and "-" not in url.split("/")[-1]:
                                image_urls.append(url)
                                break

            return image_urls

        except Exception as e:
            print(f"Error while extracting image URLs: {e}")
            return []

        finally:
            driver.quit()

    def crawl(self):
        """Crawl pages, prioritizing links containing the keyword."""
        pages_crawled = 0

        while self.queue and pages_crawled < self.max_pages:
            priority, url, from_page = heapq.heappop(self.queue)  # Get the highest-priority URL
            if url in self.visited:
                continue

            if not self.in_domain(url):
                continue

            #canonical_url = urlcanon.parse_url(url)

            print(f"Crawling (Priority {priority}): {url}")
            result = self.fetch_page(url)
            if result is None:
                helper.log_info(f"fFailed to fetch: {url}.")
                continue

            page, status_code, accessed_time, page_type_code = result

            if page is not None and status_code == 200:
                hash = hasher.min_hash(page)
                # Get the canonical URL of the page
                canonical_url = self.get_canonical_url(page, url)

                # If the canonical URL is different from the current URL, prioritize the canonical URL
                if canonical_url and canonical_url != url:
                    print(f"Canonical URL found: {canonical_url}")
                    if canonical_url in self.visited:
                        print(f"Skipping already visited canonical URL: {canonical_url}")
                        continue
                    else:
                        # Mark both the original URL and the canonical URL as visited
                        self.visited.add(url)
                        self.visited.add(canonical_url)
                        url = canonical_url  # Crawl the canonical URL instead
                else:
                    # No canonical URL or it's the same as the current URL
                    self.visited.add(url)

                hash = hashlib.sha256(page.encode('utf-8')).hexdigest() # TODO: BONUS POINTS use Locality-sensitive hashing method

                if page_type_code == 'BINARY':
                    page = url # ne vem kaj je fora

                current_page_id = db_handler.insert_page(site_id, page_type_code, url, hash, page, status_code, accessed_time, from_page)

                # Insert each image into the database
                image_urls = self.extract_image_urls_with_selenium(url)
                print(f"IMG Extracted {len(image_urls)} image URLs from {url}")

                for img_url in image_urls:
                    try:
                        # Insert the image URL into the database (page_id, filename, content_type, data, accessed_time)
                        db_handler.insert_image(current_page_id, "https://www.kulinarika.net"+img_url, "BINARY", None, accessed_time)
                        print(f"Inserted image URL: {img_url}")
                    except Exception as e:
                        print(f"Error inserting image URL {img_url}: {e}")

                # URSA: Check if current_page_id is valid, otherwise skip this page
                if current_page_id is None or current_page_id == 0:
                    helper.log_error(f"Invalid page ID for URL: {url}. Skipping...")
                    continue


            self.visited.add(url)
            pages_crawled += 1

            url_parts = urlsplit(url)
            base_url = url_parts.scheme + "://" + url_parts.netloc
            links = self.extract_links(page, base_url)
            print("  - Found", len(links), "links")
            for link, link_tag in links:
                normalized_link = self.normalize_url(link)
                if normalized_link not in self.visited:
                    priority = self.priority(page, normalized_link, link_tag)
                    heapq.heappush(self.queue, (priority, normalized_link, current_page_id))


seed = "https://www.kulinarika.net/recepti/seznam/sladice/"  # Replace with an actual URL
# TODO: Implement canonozation
#canonized_seed = urlcanon.parse_url(seed)
#site_id = db_handler.insert_or_get_site_id(canonized_seed)
canonical_seed = PreferentialWebCrawler(seed, "").normalize_url(seed)
site_id = db_handler.insert_or_get_site_id(canonical_seed)
keyword = "torta"  # Prioritize links containing this keyword
crawler = PreferentialWebCrawler(seed, keyword, max_pages=6)
crawler.crawl()

