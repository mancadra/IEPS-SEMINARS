import requests, datetime
from datetime import datetime
from min_hash import MinHasher
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
from selenium.common.exceptions import WebDriverException

class Tester():

    def fetch_page_selenium(url, image_driver = 'Firefox'):

        try:
            if image_driver == 'Chrome':
                options = ChromeOptions()
                options.add_argument("--headless")  # Run in headless mode
                driver = webdriver.Chrome(options=options)

            elif image_driver == 'Firefox':
                options = FirefoxOptions()
                options.add_argument("--headless")  # Run in headless mode
                driver = webdriver.Firefox(options=options)

            driver.get(url)  # Fetch page with Selenium
            page_content = driver.page_source.encode('utf-8')
            driver.quit()

            return page_content, 0, 'binary'

        except WebDriverException as e:
            print("Here!")
        return None
    
    def test_min_hash():

        m = MinHasher(shingle_size=3, hash_number=1000) 

        (content1, _, _) = Tester.fetch_page_selenium("https://www.kulinarika.net/recepti/seznam/sladice")
        time.sleep(5)
        (content2, _, _) = Tester.fetch_page_selenium("https://www.kulinarika.net/recepti/seznam/sladice/pecivo?offset=0")

        hash1 = m.min_hash(content1)
        hash2 = m.min_hash(content2)
        print(m.min_hash_similarity(hash1, hash2))
        print(m.jacard_similarity(content1, content2))

    def compare_db_hash_values():
        m = MinHasher(shingle_size=3, hash_number=250) 

        with open("hash_log.txt", "r") as file:
            read_lines = file.read().split("\n")
            hashes = dict()
            for l in read_lines:
                pair = l.split(" : ")
                if len(pair) == 2:
                    hashes[pair[0]] = pair[1]

        for key1 in hashes:
            for key2 in hashes:
                if key1 != key2:
                    print(key1)
                    print(key2)
                    print("Similarity estimate: ", m.min_hash_similarity(hashes[key1], hashes[key2]), "\n")