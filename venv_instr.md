Setup:
Run setup.py to create virtual enviroment, install dependencies, create config.ini

py setup_env.py
or run the following commands:

Create a virtual environment by running:

py -m venv venv
Activate your virtual environment and run:

.\.venv\Scripts\activate
Then run to install dependencies:

pip install -r requirements.txt
or

py -m pip install -r requirements.txt
To add new dependencies, run:

pip freeze > requirements.txt