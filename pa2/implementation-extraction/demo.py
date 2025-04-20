# A demo script that allows us to test the retriever
from db_handler import DbHandler
from helper import Helper

helper = Helper()
config = helper.get_config()
db = DbHandler()

queries = [
    # Relevant
    'Podaj mi recept za medene rezine',
    'Recept za skutno lažnivko',
    'Kako se naredi potratno toro',
    'Vrni mi recept za sacher torto',
    'Navodila za zebrino pecivo',
    
    # Z besedo sestavine
    'Podaj mi sestavine za medene rezine',
    'Sestavine za skutno lažnivko',
    'Katere sestavine potrebujemo za potratno toro',
    'Vrni mi sestavine za sacher torto',
    'Sestavine za zebrino pecivo',
    
    # Z besedo postopek
    'Podaj mi postopek za medene rezine',
    'Postopek za skutno lažnivko',
    'Kakšen je postopek potratno torto',
    'Vrni mi postopek za sacher torto',
    'Postopek za zebrino pecivo',
    
    # Z besedo priprava
    'Kako se pripravi medene rezine',
    'Priprava skutne lažnivke',
    'Kakšna je priprava potratne torte',
    'Vrni mi pripravo za sacher torto',
    'Priprava za zebrino pecivo',
]

similarity_metric = config['MODEL']['SIMILARITY_METRIC']
table_name = 'crawldb.page_segment'
for query in queries:
    print(f"\nQuery: {query}")
    print(db.query_similarity(query, table_name, similarity_metric))
