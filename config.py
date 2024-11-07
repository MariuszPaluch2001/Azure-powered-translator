import os

from dotenv import load_dotenv
from flask_bootstrap import Bootstrap5

from flask_wtf import CSRFProtect


class ConfigClass:
    def __init__(self, app):
        app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

        self.bootstrap = Bootstrap5(app)
        self.csrf = CSRFProtect(app)

        load_dotenv()

        self.key = os.getenv("AZURE_KEY")
        self.endpoint = os.getenv("ENDPOINT")
        self.location = os.getenv("LOCATION")
        self.path = os.getenv("PATH_ENDPOINT")
        self.is_debug = os.getenv("IS_DEBUG") == "TRUE"
        self.constructed_url = self.endpoint + self.path
