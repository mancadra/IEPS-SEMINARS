import psycopg2
import threading
from helper import Helper
import requests
import re

helper = Helper()
config = helper.get_config()
lock = threading.Lock()

class DbHandler:
    def __init__(self, dbname='crawl', user='user', password='CrawlPassword', host='localhost', port=5434):
        #def __init__(self, dbname='crawl', user='user', password='CrawlPassword', host='localhost', port=5434):
        #def __init__(self, dbname=config['DATABASE']['DB_NAME'], user=config['DATABASE']['USER'], password=config['DATABASE']['PASSWORD'], host=config['DATABASE']['HOST'], port=['DATABASE']['PORT']):
        self.conn_details = {
            'dbname': dbname,
            'user': user,
            'password': password,
            'host': host,
            'port': port,
        }
        self.conn = psycopg2.connect(**self.conn_details)
        self.conn.autocommit = True

    # TODO: fix the config file
    # TODO: Threading?, Insertion in bulk?

    def get_robots_content(self, domain):
        # TODO: Tukaj popravi da je domain samo https://www.kulinarika.net brez /recepti/seznam/sladice/ ker drugače ne najde
        # popravljeno z regularnim izrazom: + je da matches one or more, ^ je negacija => [^/]+ matches one or more stvari, ki niso /
        try:
            response = requests.get(f"{re.search(r"https?://[^/]+/", domain).group(0)}/robots.txt", timeout=10)
            # print("Response: ", response.text)
            if response.status_code == 200:
                return response.text
        except requests.RequestException as e:
            helper.log_error(e)
        return None

    def get_sitemap_content(self, domain):
        try:
            # isto kot zgoraj z regularnimi popravljeno
            response = requests.get(f"{re.search(r"https?://[^/]+/", domain).group(0)}/sitemap.xml", timeout=10)
            if response.status_code == 200:
                return response.text
        except requests.RequestException as e:
            helper.log_error(e)
        return None

    def insert_or_get_site_id(self,domain):
        cur = self.conn.cursor()
        with lock:
            cur.execute("SELECT id FROM crawldb.site WHERE domain = %s;", (domain,))
            result = cur.fetchone()

            if result:
                return result[0]
            else:
                robots = self.get_robots_content(domain)
                sitemap_content = self.get_sitemap_content(domain)

                cur.execute("INSERT INTO crawldb.site (domain, robots_content, sitemap_content) VALUES (%s,%s,%s) RETURNING id;", (domain, robots, sitemap_content,))
                return cur.fetchone()[0]

    # html_content_or_data hold either everything inside <html>, meanwhile data holds only a link to urls of images and binary data
    def insert_page(self, site_id, page_type_code, url, hash, html_content_or_data, http_status_code, accessed_time, from_page):
        to_page = None
        cur = self.conn.cursor()
        with lock:
            cur.execute("SELECT id FROM crawldb.page WHERE hash = %s", (hash,))
            duplicate = cur.fetchone()
            if duplicate:
                helper.log_info(f"Duplicate found for {url}.")
                page_type_code = "DUPLICATE"
                # TODO: Ali je to v redu da v html_content dodamo link katerga dupliciramo?
                cur.execute("""INSERT INTO crawldb.page (site_id, page_type_code, url, hash, html_content, http_status_code, accessed_time)
                                    VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id""", (site_id, page_type_code, url, hash, duplicate[0], http_status_code, accessed_time,))
                to_page = cur.fetchone()[0]

            else:
                if page_type_code == 'HTML' or page_type_code == 'UNKNOWN':
                    cur.execute("""INSERT INTO crawldb.page (site_id, page_type_code, url, hash, html_content, http_status_code, accessed_time)
                                                    VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id""",
                                (site_id, page_type_code, url, hash, html_content_or_data, http_status_code, accessed_time,))
                    to_page = cur.fetchone()[0]

                # TODO: Če je binary? Kaj pa če je frontier? (duplicate ne ker to tuki nastavljamo?)
                else:
                    cur.execute("""INSERT INTO crawldb.page (site_id, page_type_code, url, hash, html_content, http_status_code, accessed_time)
                                                                    VALUES (%s,%s,%s,%s,NULL,%s,%s) RETURNING id""",
                                (site_id, page_type_code, url, hash, http_status_code, accessed_time,))
                    to_page = cur.fetchone()[0]
                    self.insert_page_data(to_page, html_content_or_data)

        # URSA: Before calling insert_link, check if from_page is valid
        if from_page is not None and from_page != 0:
            self.insert_link(from_page, to_page)
        else:
            helper.log_error(f"Invalid from_page ID: {from_page}. Skipping link insertion.")

        #self.insert_link(from_page, to_page)
        return to_page

    def insert_page_data(self, page_id, data):
        cur = self.conn.cursor()
        with lock:
            data_type_code = self.get_data_type_code(data)
            cur.execute("INSERT INTO crawldb.page_data (page_id, data_type_code, data) VALUES (%s,%s,%s)", (page_id,data_type_code,data,))

    def insert_link(self, from_page, to_page):
        with lock:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO crawldb.link (from_page, to_page) VALUES (%s,%s)", (from_page, to_page,))

    def insert_image(self, page_id, filename, content_type, data, accessed_time):
        with lock:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO crawldb.image (page_id, filename, content_type, data, accessed_time) VALUES (%s,%s,%s,%s,%s)", (page_id, filename, content_type, data, accessed_time,))