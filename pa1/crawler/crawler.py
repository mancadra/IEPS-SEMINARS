from urllib.parse import urlsplit
import requests
from bs4 import BeautifulSoup
import heapq
from db_handler import DbHandler
import hashlib
from datetime import datetime
from helper import Helper
from min_hash import MinHasher

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

                if page_type_code == 'BINARY':
                    page = url

                current_page_id = db_handler.insert_page(site_id, page_type_code, url, hash, page, status_code, accessed_time, from_page)

            self.visited.add(url)
            pages_crawled += 1

            url_parts = urlsplit(url)
            base_url = url_parts.scheme + "://" + url_parts.netloc
            links = self.extract_links(page, base_url)
            print("  - Found", len(links), "links")
            for link, link_tag in links:
                if link not in self.visited:
                    # canonical_url = urlcanon.parse_url(link)
                    #if (link != canonical_url):
                        #print("Url: ", link, "Canonized Url: ", canonical_url)
                    priority = self.priority(page, link, link_tag)
                    heapq.heappush(self.queue, (priority, link, current_page_id))


seed = "https://www.kulinarika.net/recepti/seznam/sladice/"  # Replace with an actual URL
# TODO: Implement canonozation
#canonized_seed = urlcanon.parse_url(seed)
#site_id = db_handler.insert_or_get_site_id(canonized_seed)
site_id = db_handler.insert_or_get_site_id(seed)
keyword = "sladice"  # Prioritize links containing this keyword
crawler = PreferentialWebCrawler(seed, keyword, max_pages=5)
crawler.crawl()

