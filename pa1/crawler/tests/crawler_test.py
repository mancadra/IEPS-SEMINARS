import requests
from bs4 import BeautifulSoup
import re, csv
from tenacity import retry, stop_after_attempt, wait_exponential
from queue import Queue
import threading

target_url = "https://www.scrapingcourse.com/ecommerce/"

# instantiate the queues
high_priority_queue = Queue()
low_priority_queue = Queue()

# add the initial URL to the queues
high_priority_queue.put(target_url)
low_priority_queue.put(target_url)

# define a thread-safe set for visited URLs
visited_urls = set()
visited_lock = threading.Lock()

# set maximum crawl limit
max_crawl = 20

# create a regex pattern for product page URLs
url_pattern = re.compile(r"/page/\d+/")

# list to store scraped data
product_data = []

# activate thread lock to prevent race conditions
data_lock = threading.Lock()

# initialize session
session = requests.Session()


# implement a request retry
@retry(
    stop=stop_after_attempt(4),  # max retries
    wait=wait_exponential(multiplier=5, min=4, max=5),  # exponential backoff
)
def fetch_url(url):
    response = session.get(url)
    response.raise_for_status()
    return response


def crawler():
    # set a crawl counter to track the crawl depth
    crawl_count = 0

    while (
        not high_priority_queue.empty() or not low_priority_queue.empty()
    ) and crawl_count < max_crawl:

        # update the priority queue
        if not high_priority_queue.empty():
            current_url = high_priority_queue.get()
        elif not low_priority_queue.empty():
            current_url = low_priority_queue.get()
        else:
            break

        with visited_lock:
            if current_url in visited_urls:
                continue

            # add the current URL to the URL set
            visited_urls.add(current_url)

        # request the target URL
        response = fetch_url(current_url)

        # parse the HTML
        soup = BeautifulSoup(response.content, "html.parser")

        # collect all the links
        for link_element in soup.find_all("a", href=True):
            url = link_element["href"]

            # check if the URL is absolute or relative
            if not url.startswith("http"):
                absolute_url = requests.compat.urljoin(target_url, url)
            else:
                absolute_url = url

            with visited_lock:
                # ensure the crawled link belongs to the target domain and hasn't been visited
                if (
                    absolute_url.startswith(target_url)
                    and absolute_url not in visited_urls
                ):
                    # prioritize product pages 
                    if url_pattern.search(absolute_url):
                        high_priority_queue.put(absolute_url)
                    else:
                        low_priority_queue.put(absolute_url)

        # extract content only if the current URL matches the regex page pattern
        if url_pattern.search(current_url):
            # get the parent element
            product_containers = soup.find_all("li", class_="product")

            # scrape product data
            for product in product_containers:

                data = {
                    "Url": product.find("a", class_="woocommerce-LoopProduct-link")[
                        "href"
                    ],
                    "Image": product.find("img", class_="product-image")["src"],
                    "Name": product.find("h2", class_="product-name").get_text(),
                    "Price": product.find("span", class_="price").get_text(),
                }
                with data_lock:
                    # append extracted data
                    product_data.append(data)

        # update the crawl count
        crawl_count += 1


# specify the number of threads to use
num_workers = 4
threads = []

# start worker threads
for _ in range(num_workers):
    thread = threading.Thread(target=crawler, daemon=True)
    threads.append(thread)
    thread.start()

# wait for all threads to finish
for thread in threads:
    thread.join()

# save data to CSV
csv_filename = "products.csv"
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Url", "Image", "Name", "Price"])
    writer.writeheader()
    writer.writerows(product_data)