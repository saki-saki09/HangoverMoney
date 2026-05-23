import os
import sys


def get_base_path():

    # Running as EXE
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)

    # Running in VS Code
    return os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )


BASE_DIR = get_base_path()

# ----------------------------------------
# APP DATA FOLDER
# ----------------------------------------

APP_DATA_DIR = os.path.join(
    os.getenv("APPDATA"),
    "Hangover Money"
)

os.makedirs(APP_DATA_DIR, exist_ok=True)

# ----------------------------------------
# LOGS
# ----------------------------------------

LOGS_DIR = os.path.join(
    APP_DATA_DIR,
    "logs"
)

os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE = os.path.join(
    LOGS_DIR,
    "app.log"
)

# ----------------------------------------
# DATA
# ----------------------------------------

DATA_DIR = os.path.join(
    APP_DATA_DIR,
    "data"
)

os.makedirs(DATA_DIR, exist_ok=True)

EXPENSES_FILE = os.path.join(
    DATA_DIR,
    "expenses.json"
)

CATEGORIES_FILE = os.path.join(
    DATA_DIR,
    "categories.json"
)

CONFIG_FILE = os.path.join(
    DATA_DIR,
    "config.json"
)

# ----------------------------------------
# EXPORTS
# ----------------------------------------

EXPORTS_DIR = os.path.join(
    APP_DATA_DIR,
    "exports"
)

os.makedirs(EXPORTS_DIR, exist_ok=True)



import json


# ----------------------------------------
# DEFAULT SETTINGS
# ----------------------------------------

DEFAULT_SETTINGS = {
    "theme": "dark"
}


def initialize_config():

    if not os.path.exists(CONFIG_FILE):

        with open(CONFIG_FILE, "w") as file:

            json.dump(
                DEFAULT_SETTINGS,
                file,
                indent=4
            )


def load_config():

    initialize_config()

    with open(CONFIG_FILE, "r") as file:

        return json.load(file)


def save_config(config_data):

    with open(CONFIG_FILE, "w") as file:

        json.dump(
            config_data,
            file,
            indent=4
        )


def get_setting(key):

    config = load_config()

    return config.get(key)


def set_setting(key, value):

    config = load_config()

    config[key] = value

    save_config(config)