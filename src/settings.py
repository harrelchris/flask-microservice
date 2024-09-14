import os
import pathlib

import dotenv

BASE_DIR = pathlib.Path(__file__).resolve().parent

dotenv.load_dotenv(dotenv_path=BASE_DIR.parent / ".env")

DEBUG = os.environ.get("FLASK_DEBUG", False)

SECRET_KEY = os.environ["SECRET_KEY"]

STATIC_FOLDER = BASE_DIR / "static"

TEMPLATE_FOLDER = BASE_DIR / "templates"

STATIC_URL_PATH = None

STATIC_HOST = None

HOST_MATCHING = False

SUBDOMAIN_MATCHING = False

INSTANCE_PATH = None

INSTANCE_RELATIVE_CONFIG = False

ROOT_PATH = None
