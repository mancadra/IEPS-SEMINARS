# A demo script that allows us to test the retriever
from db_handler import DbHandler
from helper import Helper

helper = Helper()
config = helper.get_config()
db = DbHandler()

queries = [
    # Time-related questions
    'Koliko časa traja peka rolade?',
    'Ali je potrebno rolado ohladiti pred nanosom nadeva?',
    'Koliko časa vzame priprava rolade od začetka do konca?',
    'Koliko časa nam vzame priprava rolade?',

    # Ingredient questions
    'Katere sestavine so potrebne za kremo v roladi?',
    'Kakšne so sestavine za potratno rolado?',
    'Kakšne so sestavine za rolado?',
    'Ali lahko v roladi uporabim brezglutensko moko?',
    'Kakšne so sestavine za čokoladno rolado?',

    # Process/step questions
    'Kako narediti kremo za rolado?',
    'Kakšen je postopek za pripravo biskvita za rolado?',
    'Kakšen je postopek za pripravo biskvita za potratno rolado?',
    'Kako pripraviti biskvit za potratno rolado?'                   
    'Kakšen je postopek za pripravo rolade?',
    # Difficulty questions
    'Je rolada primerna za začetnike?',
    'Kakšna je težavnost priprave rolade?',
    'Ali je priprava potratne rolade zahtevna?',
    'Ali je rolado enastavno speči?',
    'Kako težko je narediti rolado?',

    # General questions
    'Pri kolikšni temperaturi pečemo rolado?',

    # Specific component questions
    'Kakšen je idealen čas za stepanje jajc za biskvit?',
    'Ali moram rolado prevrniti takoj po peki?',
    'Kako narediti čokoladno glazuro za rolado?',

    # Short keyword queries (relevance testing)
    'Rolada',
    'Biskvit',
    'Krema',
    'Potratna rolada',
    'Čokoladna rolada',

    'Kako preveriti, ali je rolada pečena?',
    'Kakšna je idealna debelina biskvita za rolado?',
    'Ali je lažje pripraviti rolado ali štrudlji?',
    'Ali lahko v roladi nadomestim maslo z oljem?',
    'Kako dolgo mora rolada počivati pred serviranjem?',
    'Kako pravilno zviti rolado, da ne razpade?',
]

similarity_metric = config['MODEL']['SIMILARITY_METRIC']
table_name = 'crawldb.page_segment'
for query in queries:
    print(f"\nQuery: {query}")
    print(db.query_similarity(query, table_name, similarity_metric))
