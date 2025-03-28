# Opis Projekta

Projekt `pa1` je preferenčni spletni pajek, ki se uporablja za ekstrakcijo podatkov o receptih sladic in analizo spletne strani [https://www.kulinarika.net/recepti/seznam/sladice/](https://www.kulinarika.net/recepti/seznam/sladice/).

## Navodila za namestitev in zagon

### Namestitev

Za zagon projekta `pa1` morate imeti nameščen Python, PostgreSQL in Docker. Poskrbite, da so na sistemu nameščene vse potrebne knjižnice. Te dobite v datoteki `requirements.txt`. Po potrebi lahko ustvarite tudi virtual environment na sledeč način
```bash
py -m venv .venv
```
in ga zaženete s spodnjim ukazom
```bash
.\.venv\Scripts\activate
```
Knjižnjice naložite z zagonom izraza 
```bash
pip install -r requirements.txt
```
Docker container ustvarite z naslednjim ukazom
```bash
docker run --name <ime_containerja> \
-e POSTGRES_PASSWORD=<vase_geslo>\
-e POSTGRES_USER=<vas_username> \
-e POSTGRES_DB=<ime_vase_baze> \
-v //c/<pot_do_folderja_pa1>/pa1/db/pgdata:/var/lib/postgresql/data \
-v //c/<pot_do_folderja_pa1>/pa1/db/init-scripts:/docker-entrypoint-initdb.d \
-p 5434:5432 \
-d pgvector/pgvector:pg16
```
Vrata in vse v zašiljenih oklepajih priredite sebi.
Po ustvarjenem docker containerju, ga povežite s PostgreSQL na vašem sistemu.

Ustvarite datoteko `config.ini` znotraj mape `crawler` in prilagodite parametre. Ta naj izgleda tako
```
[DATABASE]
DB_NAME = <ime_vase_baze>
USER = <vas_username>
PASSWORD = <vase_geslo>
HOST = localhost
PORT = 5434

[CRAWL]
START_PATH = https://www.kulinarika.net/recepti/seznam/sladice/
MAX_PAGES = 10
TIMEOUT = 5
KEYWORDS = sladice
KEYWORDS_EXCLUDED = forumi, tema, fotoalbumi, iskanje, besede
WORKERS = 4
IMAGE_DRIVER = Chrome

[HASH]
SHINGLE_SIZE = 5
HASH_NUMBER = 250
```

### Zagon
Ko imate vse pripravljeno, poženite datoteko `crawler.py`.

