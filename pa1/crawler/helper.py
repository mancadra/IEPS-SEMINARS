import os
import logging
import configparser
class Helper:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(os.path.dirname(__file__), '..', '..', 'config.ini'))

        self.LOG_DIR = os.path.join(os.path.dirname(__file__), '..', '..', "logs")
        self.LOG_FILE = os.path.join(self.LOG_DIR, "app.log")
        os.makedirs(self.LOG_DIR, exist_ok=True)

        logging.basicConfig(
            level=logging.INFO,
            filename=self.LOG_FILE,
            filemode="a",
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%d-%m-%Y %H:%M:%S",
            encoding="utf-8"
        )

    def get_config(self):
        return self.config

    def log_info(self, message):
        logging.info(message)

    def log_error(self, message):
        logging.error(message)