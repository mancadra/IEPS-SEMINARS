from urllib.parse import urlsplit, urlunsplit, urlencode, parse_qsl
from bs4 import BeautifulSoup
from db_handler import DbHandler
from datetime import datetime
from helper import Helper
from min_hash import MinHasher
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
from selenium.common.exceptions import WebDriverException
from threading import Lock
import threading
import re
import copy
from frontier import Frontier

hasher = MinHasher(shingle_size=3, hash_number=250)
helper = Helper()
config = helper.get_config()
max_pages = 10
TIMEOUT = 5

db_handler = DbHandler()

class PreferentialWebCrawler:
    def __init__(self, seed_url, max_pages=30, workers=4, image_driver='Chrome', keywords = ["sladice"], keywords_excluded = ["forumi", "tema"]):
        self.workers = workers
        self.keywords_excluded = keywords_excluded
        self.image_driver = image_driver
        self.keywords = keywords
        self.max_pages = max_pages
        self.pages_crawled = 0
        self.pages_crawled_lock = Lock()
        self.time_last_visited = time.time()
        self.timeout_lock = Lock()

        if seed_url is None:
            self.frontier = Frontier("")
            seed_url = self.frontier.restart()
        else:
            self.frontier = Frontier(seed_url)

        self.site_id = db_handler.insert_or_get_site_id(seed_url)
        url_parts = urlsplit(seed_url)
        self.domain = url_parts.scheme + "://" + url_parts.netloc


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


    def extract_urls_bs4(self, page_source):
        soup = BeautifulSoup(page_source, "html.parser")

        # Locate the <div id="fotografije"> container using BeautifulSoup
        fotografije_container = soup.find("div", id="fotografije")

        # Extract image URLs using BeautifulSoup
        bs4_image_urls = set()
        if fotografije_container:  # Ensure the container exists
            for img in fotografije_container.find_all("img"):
                data_default = img.get("data-default")
                if data_default and data_default.endswith(".webp"):
                    bs4_image_urls.add(data_default)
                else:
                    data_srcset = img.get("srcset")
                    if data_srcset:
                        srcset_urls = data_srcset.split(", ")
                        for url_1 in srcset_urls:
                            if url_1.strip().endswith(".webp") and "-" not in url_1.split("/")[-1]:
                                bs4_image_urls.add(url_1)
                                break

        bs4_image_urls = list(bs4_image_urls)
        return bs4_image_urls


    def fetch_page(self, url):
        """Fetch page content from a URL. Only one page can be accessed every TIMEOUT seconds.
            image_urls_list, page_content, 200, accessed_time, page_type_code
        """
        with self.timeout_lock:
            t = time.time()
            if t - self.time_last_visited < TIMEOUT:
                time.sleep(TIMEOUT - (t - self.time_last_visited))

            try:
                if self.image_driver == 'Chrome':
                    options = ChromeOptions()
                    options.add_argument("--headless")  # Run in headless mode
                    driver = webdriver.Chrome(options=options)

                elif self.image_driver == 'Firefox':
                    options = FirefoxOptions()
                    options.add_argument("--headless")  # Run in headless mode
                    driver = webdriver.Firefox(options=options)

                accessed_time = datetime.now()
                driver.get(url)  # Fetch page with Selenium
                content_type = driver.execute_script("return document.contentType || 'text/html'")
                self.time_last_visited = time.time()
                page_content = driver.page_source.encode('utf-8')
                driver.quit()

                page_type_code = self.get_page_type(content_type)

                return page_content, 200, accessed_time, page_type_code

            except WebDriverException as e:
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

        while self.pages_crawled < self.max_pages - (self.workers - 1):
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
                    page = url # if we have a binary file, instead of storing binary data we store it's link

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

                current_page_id = db_handler.insert_page(self.site_id, page_type_code, url, hash, page.decode('utf-8'), status_code, accessed_time, from_page)
                if from_page != 0:
                    db_handler.insert_link = (current_page_id, from_page)

                # Add links to frontier
                url_parts = urlsplit(url)
                base_url = url_parts.scheme + "://" + url_parts.netloc
                links = self.extract_links(page, base_url)
                print("  - Found", len(links), "links")
                items = []
                for link, _ in links:
                    normalized_link = self.normalize_url(link)
                    priority = self.priority(normalized_link)
                    items.append((priority, normalized_link, current_page_id))
                
                # nisem ziher če rabimo already visited
                already_visited = self.frontier.put(items)

                # Insert each image into the database
                image_urls = self.extract_urls_bs4(page)

                for img_url in image_urls:
                    try:
                        # Insert the image URL into the database (page_id, filename, content_type, data, accessed_time)
                        db_handler.insert_image(current_page_id, "https://www.kulinarika.net" + img_url, "BINARY", None, accessed_time)
                        #print(f"Inserted image URL: {img_url}")
                    except Exception as e:
                        print(f"Error inserting image URL {img_url}: {e}")

                # URSA: Check if current_page_id is valid, otherwise skip this page
                if current_page_id is None or current_page_id == 0:
                    helper.log_error(f"Invalid page ID for URL: {url}. Skipping...")
                    continue

            with self.pages_crawled_lock:
                self.pages_crawled += 1

db_handler.clear_db()
start_time = time.time()
seed = "https://www.kulinarika.net/recepti/seznam/sladice/"  # Replace with an actual URL
# seed = "https://www.kulinarika.net/recepti/sladice/torte/cokoladna-torta-presna-veganska-/16802"
crawler = PreferentialWebCrawler(seed, max_pages, image_driver='Firefox')
# crawler = PreferentialWebCrawler(None, max_pages, image_driver='Firefox')
crawler.run()
end_time = time.time()
execution_time = end_time - start_time
print(f"{max_pages} crawled in {execution_time:.6f} seconds.")

