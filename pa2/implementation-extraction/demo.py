# A demo script that allows us to test the retriever
from db_handler import DbHandler
from transformers import AutoTokenizer, AutoModelForMaskedLM

# TODO: Rešiti problem, da npr. sestavine in priprava ponavadi nista povezana oz. ne vsebujejo ključne besede npr. "potratna rolada" v poizvedbi, ki ločuje recepte med sabo
# TODO: Popraviti sklanjatev za čas priprave "Za recept porabimo 1 ura."
# TODO: Popravi problem, saj npr. pri poizvedbi 'Kakšen je postopek za pripravo biskvita za rolado?' vrnemo postopek šele kot 5. rezultat, saj se npr. bisvit pojavi v sestavinah, rolada v opisu in to prej zazna? Mogoče rešitev, če pri cosinus similarity upoštevamo še tip segmenta? Ali pa da pred vsakim segmentom, ki ga shranimo dopišemo h kateremu naslovi spada npr. Potratna rolada: Priprava ....
# TODO: Postopek vrača šele kot zadnji rezultat, ker v samem postopku ni nikjer besede postopek...
# TODO: Preveri še druge modele

db = DbHandler()

queries = [
    # Time-related questions
    'Koliko časa traja peka rolade?',
    'Ali je potrebno rolado ohladiti pred nanosom nadeva?',
    'Koliko časa vzame priprava rolade od začetka do konca?',
    'Koliko časa nam vzame priprava rolade?',

    # Ingredient questions
    'Katere sestavine so potrebne za kremo v roladi?',
    'Kakšne so sestavine za potratno rolado?',                      # 2. rezultat je pravilen(sestavine)
    'Kakšne so sestavine za rolado?',                               # 2. rezultat je pravilen(sestavine)
    'Ali lahko v roladi uporabim brezglutensko moko?',
    'Kakšne so sestavine za čokoladno rolado?',

    # Process/step questions
    'Kako narediti kremo za rolado?',                               # Nismo dobili postopka
    'Kakšen je postopek za pripravo biskvita za rolado?',           # Dobimo kot 5. rezultat
    'Kakšen je postopek za pripravo biskvita za potratno rolado?',  # Dobimo kot 5. rezultat
    'Kako pripraviti biskvit za potratno rolado?'                   # 2. rezultat je pravilen(postopek)
    'Kakšen je postopek za pripravo rolade?',                       # Ne dobimo postopka

    # Difficulty questions
    'Je rolada primerna za začetnike?',
    'Kakšna je težavnost priprave rolade?',
    'Ali je priprava potratne rolade zahtevna?',
    'Ali je rolado enastavno speči?',
    'Kako težko je narediti rolado?',

    # General questions
    'Pri kolikšni temperaturi pečemo rolado?',                      # Dobimno za buhtelje

    # Specific component questions
    'Kakšen je idealen čas za stepanje jajc za biskvit?',           # Ne dobimo postopka
    'Ali moram rolado prevrniti takoj po peki?',                    # Dobimo postopek za rolado
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
    'Kako dolgo mora rolada počivati pred serviranjem?'
    'Kako pravilno zviti rolado, da ne razpade?',                   # Na 2. mestu vrača postopek za rogljičke
]


model_name = 'labse'                 # 'labse' , 'sloberta' , 'openai'
table_name = 'crawldb.page_segment'
for query in queries:
    print(f"\nQuery: {query}")
    print(db.query_db_cosine(query, model_name, table_name))
