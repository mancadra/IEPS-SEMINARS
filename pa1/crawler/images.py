from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import bs4

# Questions: why do we need browser drivers in selenium?
# Browser Drivers:
#   Selenium doesn't directly control browsers. Instead, it uses a browser-specific driver (e.g., ChromeDriver for Chrome, GeckoDriver for Firefox) to communicate with the browser.
#   These drivers act as a bridge between Selenium and the browser.

#driver = webdriver.Chrome(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode so that he doesnt open the chrome browser.

driver = webdriver.Chrome(options=chrome_options)
url2 = "https://www.kulinarika.net/recepti/sladice/pecivo/cokoladno-mascarponejeve-kocke/12619/"
url1 = "https://www.kulinarika.net/recepti/sladice/pecivo/potratna-rolada/22765/"
url = "https://www.kulinarika.net/recepti/sladice/torte/cokoladna-torta-presna-veganska-/16802"
domain = "https://www.kulinarika.net"
url_ne_dela = "https://www.kulinarika.net/recepti/seznam/sladice/"
driver.get(url)

# Wait for the page to fully load (adjust the sleep time if needed)
time.sleep(5)  # Wait for JavaScript to render the content

# Locate the <div id="fotografije"> element
fotografije_div = driver.find_element(By.ID, "fotografije")

# Find all <img> tags within the <div id="fotografije">
images = fotografije_div.find_elements(By.TAG_NAME, "img")

# Extract image URLs
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
            # Example: "/slikerecepti/22765/1-200x150.webp 200w, /slikerecepti/22765/1-400x300.webp 400w, /slikerecepti/22765/1.webp"
            srcset_urls = data_srcset.split(", ")
            #print(srcset_urls)
            # Find the URL without dimensions (e.g., "/slikerecepti/22765/1.webp")
            for url in srcset_urls:
                if url.strip().endswith(".webp") and "-" not in url.split("/")[-1]:
                    image_urls.append(url)
                    break
# Get the page source and parse it with BeautifulSoup
page_source = driver.page_source
soup = bs4.BeautifulSoup(page_source, "html.parser")

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

# Convert the set to a list for comparison
bs4_image_urls = list(bs4_image_urls)


print("All image URLs:")
for i, url in enumerate(image_urls):
    print(f"{i}: ",domain+url)

print("\nbs4:")
for i, url in enumerate(bs4_image_urls):
    print(f"{i}: ",domain+url)

driver.quit()
