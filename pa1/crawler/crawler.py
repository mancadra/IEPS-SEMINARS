from urllib.parse import urlsplit, urlunsplit, urlencode, parse_qsl
import requests
from bs4 import BeautifulSoup
from db_handler import DbHandler
from datetime import datetime
from helper import Helper
from min_hash import MinHasher
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from queue import PriorityQueue
from threading import Lock
import threading
import re
from frontier import Frontier

hasher = MinHasher(shingle_size=3, hash_number=250)
helper = Helper()
config = helper.get_config()
site_id = None
current_page_id = None
max_pages = 10
TIMEOUT = 5

db_handler = DbHandler()
db_handler.clear_db()

class PreferentialWebCrawler:
    def __init__(self, seed_url, keywords, max_pages=30, workers=4, image_driver='Chrome', keywords_excluded = ["forumi", "tema"]):
        self.workers = workers
        self.keywords_excluded = keywords_excluded
        self.image_driver = image_driver
        self.seed_url = seed_url
        self.keywords = keywords
        self.max_pages = max_pages
        url_parts = urlsplit(seed_url)
        self.domain = url_parts.scheme + "://" + url_parts.netloc
        self.pages_crawled = 0
        self.pages_crawled_lock = Lock()
        self.time_last_visited = time.time()
        self.timeout_lock = Lock()
        self.frontier = Frontier(seed_url)


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
            #print(f"Extracted canonical URL: {canonical_url} (Original: {url})")
            return canonical_url

        #print(f"No canonical URL found. Using original: {url}")
        return self.normalize_url(url)


    def fetch_page(self, url):
        """Fetch page content from a URL. Only one page can be accessed every TIMEOUT seconds."""
        with self.timeout_lock:
            t = time.time()
            if t - self.time_last_visited < TIMEOUT:
                time.sleep(TIMEOUT - (t - self.time_last_visited))
            try:
                response = requests.get(url)
                self.time_last_visited = time.time()
                response.encoding = 'utf-8'
                print("Fetched page at: ", time.time())
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


    def priority(self, link):
        for k in self.keywords_excluded:
            if k in link: return 1
        for k in self.keywords:
            if k in link: return 0 # Assign priority (0 = high, 1 = lower)
        return 1


    def extract_image_urls_with_selenium(self, url, image_driver='Chrome'):
        """
        Extract image URLs using Selenium.
        """

        if image_driver == 'Chrome':
            options = ChromeOptions()
            options.add_argument("--headless")  # Run in headless mode
            driver = webdriver.Chrome(options=options)

        elif image_driver == 'Firefox':
            options = FirefoxOptions()
            options.add_argument("--headless")  # Run in headless mode
            driver = webdriver.Firefox(options=options)

        try:
            driver.get(url)

            # Wait for the page to fully load
            time.sleep(5)  # Wait for JavaScript to render the content

            # Locate the <div id="fotografije"> element
            try:
                fotografije_div = driver.find_element(By.ID, "fotografije")
            except NoSuchElementException:
                print(f"No <div id='fotografije'> found. Skipping this page: {url}.")
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


    # Runs the crawler using multiple threads
    def run(self):
        threads = []
        for _ in range(self.workers):
            thread = threading.Thread(target=self.crawl)
            thread.start()
            threads.append(thread)
        for t in threads:
            t.join()


    def crawl(self):
        """Crawl pages, prioritizing links containing the keyword."""

        while self.pages_crawled < self.max_pages:
            priority, url, from_page = self.frontier.get()  # Get the highest-priority URL
            
            if not self.in_domain(url): continue

            print(f"Crawling (Priority {priority}): {url}")
            result = self.fetch_page(url)
            if result is None:
                helper.log_info(f"fFailed to fetch: {url}.")
                continue

            page, status_code, accessed_time, page_type_code = result

            if page is not None and status_code == 200:

                hash = hasher.min_hash(page)

                canonical_url = self.get_canonical_url(page, url)   # Get the canonical URL of the page

                if page_type_code == 'BINARY':
                    page = url # ne vem kaj je fora

                # If the canonical URL is different from the current URL, prioritize the canonical URL
                if canonical_url and canonical_url != url:
                    print(f"Canonical URL found: {canonical_url}")
                    if canonical_url in self.frontier.visited:
                        print(f"Skipping already visited canonical URL: {canonical_url}")
                        continue
                    else:
                        # Mark both the original URL and the canonical URL as visited
                        self.frontier.add_visited(canonical_url)
                        url = canonical_url  # Crawl the canonical URL instead
                
                self.frontier.add_hash(url, hash)

                current_page_id = db_handler.insert_page(site_id, page_type_code, url, hash, page, status_code, accessed_time, from_page)

                # Add links to frontier
                url_parts = urlsplit(url)
                base_url = url_parts.scheme + "://" + url_parts.netloc
                links = self.extract_links(page, base_url)
                #print("  - Found", len(links), "links")
                items = []
                for link, _ in links:
                    normalized_link = self.normalize_url(link)
                    priority = self.priority(normalized_link)
                    items.append((priority, normalized_link, current_page_id))
                
                # nisem ziher če rabimo already visited
                already_visited = self.frontier.put(items)

                # Insert each image into the database
                # image_urls = self.extract_image_urls_with_selenium(url, image_driver=self.image_driver)
                image_urls = [str(time.time())]
                # print(f"IMG Extracted {len(image_urls)} image URLs from {url}")

                for img_url in image_urls:
                    try:
                        # Insert the image URL into the database (page_id, filename, content_type, data, accessed_time)
                        db_handler.insert_image(current_page_id, re.search(r'[^/]+$', img_url).group(0), "BINARY", "https://www.kulinarika.net" + img_url, accessed_time)
                        #print(f"Inserted image URL: {img_url}")
                    except Exception as e:
                        print(f"Error inserting image URL {img_url}: {e}")

                # URSA: Check if current_page_id is valid, otherwise skip this page
                if current_page_id is None or current_page_id == 0:
                    helper.log_error(f"Invalid page ID for URL: {url}. Skipping...")
                    continue

            with self.pages_crawled_lock:
                self.pages_crawled += 1

start_time = time.time()
seed = "https://www.kulinarika.net/recepti/seznam/sladice/"  # Replace with an actual URL
site_id = db_handler.insert_or_get_site_id(seed)
keywords = ["sladice"]  # Prioritize links containing this keyword
crawler = PreferentialWebCrawler(seed, keywords, max_pages)
crawler.run()
end_time = time.time()
execution_time = end_time - start_time
print(f"{max_pages} crawled in {execution_time:.6f} seconds.")

