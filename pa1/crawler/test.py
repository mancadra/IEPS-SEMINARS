import requests, datetime
from datetime import datetime
from min_hash import MinHasher

class Tester():
    
    def test_fetch_page_and_min_hash():
        def fetch_page(url):
            """Fetch page content from a URL."""
            try:
                response = requests.get(url, timeout=5)
                response.encoding = 'utf-8'
                if response.status_code == 200: 
                    accessed_time = datetime.now()
                    return response.text, response.status_code, accessed_time
            except requests.RequestException as e:
                print("Hello")
            return None

        m = MinHasher(shingle_size=3, hash_number=1000) 

        (content1, _, _) = fetch_page("https://www.kulinarika.net/recepti/sladice/pecivo/orehova-rulada/5737/")
        (content2, _, _) = fetch_page("https://www.kulinarika.net/recepti/sladice/pecivo/orehova-rulada/5737/?offset=10#mnenja")

        hash1 = m.min_hash(content1)
        hash2 = m.min_hash(content2)
        print(m.min_hash_similarity(hash1, hash2))
        print(m.jacard_similarity(content1, content2))