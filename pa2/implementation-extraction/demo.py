# A demo script that allows us to test the retriever
from db_handler import DbHandler
from helper import Helper

helper = Helper()
config = helper.get_config()
db = DbHandler()

queries = [
    'arašidovčki',
    'jabolčni kompot',
    'bananina torta',
    'bavarska krema',
    'čokoladni ježki',

    'Podaj mi recept za arašidovčke',
    'Recept za jabolčni kompot',
    'Kako se naredi bananino torto',
    'Vrni mi recept za bavarsko kremo',
    'Navodila za čokoladne ježke',
    
    # Z besedo sestavine
    'Podaj mi sestavine za arašidovčke',
    'Sestavine za jabolčni kompot',
    'Katere sestavine potrebujemo za bananino torto',
    'Vrni mi sestavine za bavarsko kremo',
    'Sestavine za čokoladne ježke',
    
    # Z besedo postopek
    'Podaj mi postopek za arašidovčke',
    'Postopek za jabolčni kompot',
    'Kakšen je postopek bananino torto',
    'Vrni mi postopek za bavarsko kremo',
    'Postopek za čokoladne ježke',
    
    # Z besedo priprava
    'Kako se pripravi arašidovčke',
    'Priprava jabolčnega kompota',
    'Kakšna je priprava bananine torte',
    'Vrni mi pripravo za bavarsko kremo',
    'Priprava za čokoladne ježke',

    'Podaj mi recepte, ki porabijo 1 uro',
    'Podaj mi recepte, ki porabijo 45 min ',
    'Podaj mi recepte, ki porabijo 15 min ',
    'Podaj mi recepte z malinami',
    'Podaj mi recepte z bananami',
    'Podaj mi čokoladna peciva',
    'Podaj mi recepte s čokolado',
    'Podaj mi recepte z nutelo',
    'Podaj mi recepte s kokosom',
    'Podaj mi recepte za valentinovo',
    'Podaj mi božične recepte',
]


queries = [
    'Vrni mi recept za sacher torto',
    'Navodila za zebrino pecivo',
    'Podaj mi zdrave recepte',
]


similarity_metric = config['MODEL']['SIMILARITY_METRIC']
table_name = 'crawldb.page_segment'
for query in queries:
    print(f"\nQuery: {query}")
    print(db.query_similarity(query, table_name, similarity_metric))
