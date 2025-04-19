from bs4 import BeautifulSoup
from lxml import html
import re
from helper import Helper
from embeddings import calculate_embedding
from db_handler import DbHandler
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModel, GPT2TokenizerFast

helper = Helper()
config = helper.get_config()

class SegmentProcessor:
    def __init__(self, model_name):
        self.db = DbHandler()
        self.dict_difficulty = {1: 'zelo lahek', 2: 'lahek', 3: 'srednje težek', 4: 'težek', 5: 'zelo težek'}

        if model_name == 'labse':
            self.model = SentenceTransformer('sentence-transformers/LaBSE')
            self.embedding_fun = lambda text: self.model.encode(text).tolist()
        elif model_name == 'sloberta':
            self.tokenizer = AutoTokenizer.from_pretrained("EMBEDDIA/sloberta")
            self.model = AutoModel.from_pretrained("EMBEDDIA/sloberta")
            self.embedding_fun = lambda text: calculate_embedding(self.model, self.tokenizer, text)
        elif model_name == 'openai':
            #tokenizer = GPT2TokenizerFast.from_pretrained('Xenova/text-embedding-ada-002')
            self.tokenizer = AutoTokenizer.from_pretrained("Xenova/text-embedding-ada-002")
            self.model = AutoModel.from_pretrained("Xenova/text-embedding-ada-002")
            self.embedding_fun = lambda text: calculate_embedding(self.model, self.tokenizer, text)
        else:
            raise ValueError(f"Unknown model type: {model_name}")


    def process_page(self, page_id):
        html_content = self.db.get_html_content(page_id)
        if not html_content:
            return False
            
        cleaned_content = self.clean_html(html_content)
        self.db.update_cleaned_content(page_id, cleaned_content)
        
        url = self.db.get_url(page_id)
        if ('?offset=' not in url) and (any(c.isdigit() for c in url)):
            print("Page id: ", page_id)
            self.process_recipe(page_id, cleaned_content)
            """
            self.process_opis(page_id, cleaned_content)
            self.process_postopek(page_id, cleaned_content)
            self.process_sestavine(page_id, cleaned_content)
            self.process_tags(page_id, cleaned_content)
            self.process_komentarji(page_id, cleaned_content)"""
            return True
        else:
            return False


    def clean_html(self, html_content):
        """Extract main recipe section"""
        soup = BeautifulSoup(html_content, 'html.parser')
        section = soup.find('section', id='recepti')
        return str(section)


    def process_recipe(self, page_id, html_content):
        """Process and store the whole recipe as one segment"""
        tree = html.fromstring(html_content)
        result_texts = []

        try:
            # 1. Extract title
            try:
                title = tree.xpath('//div[@id="recept-main"]/h1/text()')
                if title:
                    title = title[0].strip()
                    result_texts.append(f"{title}:")
            except Exception as e:
                raise Exception(f"Failed to extract title: {str(e)}")

            # 2. Extract description
            try:
                description = tree.xpath('//div[@id="recept-main"]/p/text()')
                if description:
                    description = description[0].strip()
                    result_texts.append(f"Opis recepta: {description}")
            except Exception as e:
                raise Exception(f"Failed to extract description: {str(e)}")

            # 3. Extract time
            try:
                time = re.search(r'<span class="cas">([^<]+)<\/span>', html_content)
                if time:
                    time = time.group(1).strip()
                    result_texts.append(f"Čas priprave: {time}")
            except Exception as e:
                raise Exception(f"Failed to extract time: {str(e)}")

            # 4. Extract difficulty
            try:
                difficulty = len(tree.xpath('//li[@class="zahtevnost"]/img[@src="/grafika6/ikona-utez.png"]'))
                if difficulty:
                    result_texts.append(f"Težavnost: {self.dict_difficulty.get(difficulty, 'neznana')}")
            except Exception as e:
                raise Exception(f"Failed to extract difficulty: {str(e)}")

            # 5. Extract procedure
            try:
                postopek_text = tree.xpath('//div[@id="postopek"]')
                if postopek_text:
                    postopek_text = postopek_text[0].text_content().strip()
                    result_texts.append(f"\nPostopek:\n{postopek_text}")
            except Exception as e:
                raise Exception(f"Failed to extract procedure: {str(e)}")

            # 6. Extract ingredients
            try:
                sestavine_text = []
                ingredients_all_p = tree.xpath(
                    '//div[@id="sestavine"]/p[@class="cf"] | //div[@id="sestavine"]/p[@class="cf poglavje"]')

                for p in ingredients_all_p:
                    try:
                        p0 = self.convert_units(p[0].text_content().strip().replace('\u200b', ''))
                        p1 = self.convert_units(p[1].text_content().strip().replace('\u200b', ''))

                        if 'poglavje' in p.get('class', ''):
                            sestavine_text.append(f"\n{p1}")
                        else:
                            line = f"{p0} {p1}" if p0 else p1
                            sestavine_text.append(line)
                    except Exception as e:
                        raise Exception(f"Failed to process ingredient line: {str(e)}")

                result_texts.append(f"\nSestavine:\n{'\n'.join(sestavine_text)}")
            except Exception as e:
                raise Exception(f"Failed to extract ingredients: {str(e)}")

            # 7. Extract tags
            try:
                tags_text = tree.xpath('//section[@id="recepti"]/ul[@id="servis2"]/span/a/text()')
                if tags_text:
                    result_texts.append(f"\nOznake: {', '.join(tags_text)}")
            except Exception as e:
                raise Exception(f"Failed to extract tags: {str(e)}")

            # 8. Extract comments
            try:
                authors = re.findall(r'<a\s+class="avtorMnenja"[^>]*>(.*?)<\/a>', html_content)
                comments = re.findall(r'<div\s+class="msgbody"[^>]*>(?:[^<]|<(?!p\b))*<p>(.*?)<\/p>', html_content)
                if authors and comments:
                    komentarji = [f"{a}: {k}" for a, k in zip(authors, comments)]
                    result_texts.append(f"\nKomentarji:\n{'\n'.join(komentarji)}")
            except Exception as e:
                raise Exception(f"Failed to extract comments: {str(e)}")

            # Join all parts with newlines
            recept_text = '\n'.join(result_texts)
            print(recept_text)
            embedding = self.embedding_fun(recept_text)

            self.db.insert_page_segment(
                page_id=page_id,
                page_segment=recept_text,
                embedding=embedding
            )

        except Exception as e:
            print(f"Error processing recipe (page {page_id}) at step: {str(e)}")
            raise  # Re-raise to see full traceback


    def process_opis(self, page_id, html_content):
        """Process and store description segment"""
        tree = html.fromstring(html_content)
        try:
            description = tree.xpath('//div[@id="recept-main"]/p/text()')[0].strip()
            time = re.search(r'<span class="cas">([^<]+)<\/span>', html_content).group(1).strip()
            difficulty = len(tree.xpath('//li[@class="zahtevnost"]/img[@src="/grafika6/ikona-utez.png"]'))
            
            segment_text = f"Opis recepta je '{description}'. Za recept porabimo {time}. Recept je {self.dict_difficulty[difficulty]}."
            embedding = self.embedding_fun(segment_text)

            self.db.insert_page_segment(
                page_id=page_id,
                segment_type='OPIS',
                page_segment=segment_text,
                embedding=embedding
            )
        except Exception as e:
            print(f"Error processing OPIS for page {page_id}: {str(e)}")


    def process_postopek(self, page_id, html_content):
        """Process and store procedure segment"""
        try:
            tree = html.fromstring(html_content)
            p = tree.xpath('//div[@id="postopek"]')[0].text_content().strip()
            embedding = self.embedding_fun(p)

            self.db.insert_page_segment(
                page_id=page_id,
                segment_type='POSTOPEK',
                page_segment=p,
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

            embedding = self.embedding_fun(output.strip())
            
            self.db.insert_page_segment(
                page_id=page_id,
                segment_type='SESTAVINE',
                page_segment=output.strip(),
                embedding=embedding
            )
        except Exception as e:
            print(f"Error processing SESTAVINE for page {page_id}: {str(e)}")


    def process_tags(self, page_id, html_content):
        """Process and store tags segment"""
        try:
            tree = html.fromstring(html_content)
            tags = tree.xpath('//section[@id="recepti"]/ul[@id="servis2"]/span/a/text()')
            embedding = self.embedding_fun(", ".join(tags))

            self.db.insert_page_segment(
                page_id=page_id,
                segment_type='TAGS',
                page_segment=", ".join(tags),
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
            embedding = self.embedding_fun(segment_text)

            self.db.insert_page_segment(
                page_id=page_id,
                segment_type='KOMENTARJI',
                page_segment=segment_text,
                embedding=embedding
            )
        except Exception as e:
            print(f"Error processing KOMENTARJI for page {page_id}: {str(e)}")


db_handler = DbHandler()
db_handler.clear_page_segment()
model_name = config['MODEL']['MODEL_NAME']
processor = SegmentProcessor(model_name=model_name)
for i in range(1, 7999):
    processor.process_page(i)
processor.db.create_segment_index()

print("Processing complete.")