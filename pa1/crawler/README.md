Create a virtual environment by running:
```bash
py -m venv .venv
```

Activate your virtual environment and run:
```bash
.\.venv\Scripts\activate
```

Then run to install dependencies (Make sure in venv):
```bash
pip install -r requirements.txt
```
or
```bash
py -m pip install -r requirements.txt
```

To add new dependencies, run in venv (also for first time creation of requirements.txt):
```bash
pip freeze > requirements.txt
```