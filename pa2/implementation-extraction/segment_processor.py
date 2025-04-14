from bs4 import BeautifulSoup
from lxml import html
import re
from db_handler import DbHandler
from sentence_transformers import SentenceTransformer

class SegmentProcessor:
    def __init__(self):
        self.db = DbHandler()
        self.dict_difficulty = {1: 'zelo lahek', 2: 'lahek', 3: 'srednje težek', 4: 'težek', 5: 'zelo težek'}
        self.model = SentenceTransformer('sentence-transformers/LaBSE')

    def process_page(self, page_id):
        html_content = self.db.get_html_content(page_id)
        if not html_content:
            return False
            
        cleaned_content = self.clean_html(html_content)
        self.db.update_cleaned_content(page_id, cleaned_content)
        
        url = self.db.get_url(page_id)
        if not '?offset=' in url:
            self.process_opis(page_id, cleaned_content)
            self.process_postopek(page_id, cleaned_content)
            self.process_sestavine(page_id, cleaned_content)
            self.process_tags(page_id, cleaned_content)
            self.process_komentarji(page_id, cleaned_content)
            return True
        else:
            return False

    def clean_html(self, html_content):
        """Extract main recipe section"""
        soup = BeautifulSoup(html_content, 'html.parser')
        section = soup.find('section', id='recepti')
        return str(section)

    def process_opis(self, page_id, html_content):
        """Process and store description segment"""
        tree = html.fromstring(html_content)
        try:
            description = tree.xpath('//div[@id="recept-main"]/p/text()')[0].strip()
            time = re.search(r'<span class="cas">([^<]+)<\/span>', html_content).group(1).strip()
            difficulty = len(tree.xpath('//li[@class="zahtevnost"]/img[@src="/grafika6/ikona-utez.png"]'))
            
            segment_text = f"Opis recepta je '{description}'. Za recept porabimo {time}. Recept je {self.dict_difficulty[difficulty]}."
            embedding = self.model.encode(segment_text).tolist()

            self.db.insert_page_segment(
                page_id=page_id,
                page_segment=segment_text,
                segment_type='OPIS',
                embedding=embedding
            )
        except Exception as e:
            print(f"Error processing OPIS for page {page_id}: {str(e)}")


    def process_postopek(self, page_id, html_content):
        """Process and store procedure segment"""
        try:
            tree = html.fromstring(html_content)
            p = tree.xpath('//div[@id="postopek"]')[0].text_content().strip()
            embedding = self.model.encode(p).tolist()

            self.db.insert_page_segment(
                page_id=page_id,
                page_segment=p,
                segment_type='POSTOPEK',
                embedding=embedding
            )
        except Exception as e:
            print(f"Error processing POSTOPEK for page {page_id}: {str(e)}")

    def convert_units(self, string):
        """Converts units into whole words."""
        dict_units = {'g': 'gramov', 'mg': 'miligramov', 'kg': 'kilogramov', 'dag': 'dekagramov', 'ml': 'mililitrov',
                                'l': 'litrov', 'dl': 'decilitrov'}
        string = string.split()
        new = []
        for i, n in enumerate(string):
            if i > 0 and any(c.isdigit() for c in string[i-1]) and n in dict_units:
                new.append(dict_units[n])
            else:
                new.append(n)
        return ' '.join(new)

    def process_sestavine(self, page_id, html_content):
        """Process and store ingredients segment"""
        try:
            tree = html.fromstring(html_content)
            output = ""
            ingredients_all_p = tree.xpath('//div[@id="sestavine"]/p[@class="cf"] | //div[@id="sestavine"]/p[@class="cf poglavje"]')
            
            for p in ingredients_all_p:
                p0 = self.convert_units(p[0].text_content().strip().replace('\u200b', ''))
                p1 = self.convert_units(p[1].text_content().strip().replace('\u200b', ''))
                
                if 'poglavje' in p.get('class', ''):
                    output += f"\n{p1}\n"
                else:
                    line = f"{p0} {p1}" if p0 else p1
                    output += f"{line}\n"

            embedding = self.model.encode(output.strip()).tolist()
            
            self.db.insert_page_segment(
                page_id=page_id,
                page_segment=output.strip(),
                segment_type='SESTAVINE',
                embedding=embedding
            )
        except Exception as e:
            print(f"Error processing SESTAVINE for page {page_id}: {str(e)}")

    def process_tags(self, page_id, html_content):
        """Process and store tags segment"""
        try:
            tree = html.fromstring(html_content)
            tags = tree.xpath('//section[@id="recepti"]/ul[@id="servis2"]/span/a/text()')
            embedding = self.model.encode(", ".join(tags)).tolist()

            self.db.insert_page_segment(
                page_id=page_id,
                page_segment=", ".join(tags),
                segment_type='TAGS',
                embedding=embedding
            )
        except Exception as e:
            print(f"Error processing TAGS for page {page_id}: {str(e)}")

    def process_komentarji(self, page_id, html_content):
        """Process and store comments segment"""
        try:
            authors = re.findall(r'<a\s+class="avtorMnenja"[^>]*>(.*?)<\/a>', html_content)
            comments = re.findall(r'<div\s+class="msgbody"[^>]*>(?:[^<]|<(?!p\b))*<p>(.*?)<\/p>', html_content)
            
            segment_text = "\n".join([f"{a} je zapisal '{k}'." for a, k in zip(authors, comments)])
            embedding = self.model.encode(segment_text).tolist()

            self.db.insert_page_segment(
                page_id=page_id,
                page_segment=segment_text,
                segment_type='KOMENTARJI',
                embedding=embedding
            )
        except Exception as e:
            print(f"Error processing KOMENTARJI for page {page_id}: {str(e)}")

db_handler = DbHandler()
db_handler.clear_page_segment()
processor = SegmentProcessor()
#processor.process_page(3)
processor.process_page(2)
processor.process_page(7332)
processor.db.create_segment_index()
print("Processing complete.")