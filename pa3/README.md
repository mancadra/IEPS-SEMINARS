# Question Answering API

Projekt `pa3` je integrira podatkovno bazo iz projekta `pa2` z jezikovnim modelom.
Dodan je preprost spletni vmesnik, ki omogoča uporabniku, da vnese vprašanje in prejme odgovor generiran z jezikovnim modelom.
Uporabnik se lahko odloči ali bo model prejen dodaten kontekts pridobljen iz podatkovne baze.

---

## Navodila za namestitev in zagon

### Namestitev

Za zagon projekta `pa3` morate imeti nameščen Python, PostgreSQL in Docker. Poskrbite, da so na sistemu nameščene vse potrebne knjižnice. Te dobite v datoteki `requirements.txt` znotraj glavne mape IEPS-SEMINARS. Po potrebi lahko ustvarite tudi virtual environment na sledeč način

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
Namestite ollama[https://ollama.com/] in uporabite naslednji ukazom:
```bash
ollama pull gemma3
```
Če je v datoteki `config.ini` naveden drugačen model, potem tega namestite na isti način.

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

Ustvarite datoteko `config.ini` znotraj mape `pa3` in prilagodite parametre. Ta naj izgleda tako
```
[DATABASE]
DB_NAME = <ime_vase_baze>
USER = <vas_username>
PASSWORD = <vase_geslo>
HOST = localhost
PORT = 5434

[MODEL]
; labse , sloberta, openai, croslo, distilbert
MODEL_NAME = labse
; cosine, L1, inner_product
SIMILARITY_METRIC = inner_product
; llama3.2:1b, gemma3:latest, deepseek-r1:latest
; qwen3:latest, phi4, llama4:latest; hf.co/tknez/GaMS-9B-Instruct-GGUF:latest
LANGUAGE_MODEL = gemma3:latest
CONTEXT_SIZE = 3
```

### Obnovitev baze
Povezava do kopije baze se nahaja v mapi `extraction-db`.
Po prenosu kopije, lahko bazo obnovite znotraj pgAdmina in sicer:
Z desnim klikom na bazo, ki smo jo ustvarili z docker containerjom, izberite `Restore`
Izberite preneseno datoteko. Pod query_options obklukajte `Clean before restore` in pod `Options` onemogočite `Triggers`.
Nato lahko bazo obnovite s klikom na gumb `Restore`.

---

### Zagon spletnega vmesnika

Da zaženete strežnik znotraj mape `pa3` uporabite naslednji ukaz:

```bash
python main.py
```

Aplikacija bo dostopna na spletni povezavi:
http://localhost:8000

---
