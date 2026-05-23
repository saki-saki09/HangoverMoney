import os
import sys
import json


# ---------------------------------------------------
# BASE DIRECTORY
# ---------------------------------------------------

def get_base_path():

    # Running as EXE
    if getattr(sys, "frozen", False):

        return os.path.dirname(
            sys.executable
        )

    # Running in VS Code
    return os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )


BASE_DIR = get_base_path()


# ---------------------------------------------------
# APP DATA DIRECTORY
# ---------------------------------------------------

APP_DATA_DIR = os.path.join(
    os.getenv("APPDATA"),
    "Hangover Money"
)

os.makedirs(
    APP_DATA_DIR,
    exist_ok=True
)


# ---------------------------------------------------
# LOGS DIRECTORY
# ---------------------------------------------------

LOGS_DIR = os.path.join(
    APP_DATA_DIR,
    "logs"
)

os.makedirs(
    LOGS_DIR,
    exist_ok=True
)

LOG_FILE = os.path.join(
    LOGS_DIR,
    "app.log"
)


# ---------------------------------------------------
# DATA DIRECTORY
# ---------------------------------------------------

DATA_DIR = os.path.join(
    APP_DATA_DIR,
    "data"
)

os.makedirs(
    DATA_DIR,
    exist_ok=True
)

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


# ---------------------------------------------------
# EXPORTS DIRECTORY
# ---------------------------------------------------

EXPORTS_DIR = os.path.join(
    APP_DATA_DIR,
    "exports"
)

os.makedirs(
    EXPORTS_DIR,
    exist_ok=True
)


# ---------------------------------------------------
# DEFAULT SETTINGS
# ---------------------------------------------------

DEFAULT_SETTINGS = {
    "theme": "dark"
}


DEFAULT_CATEGORIES = [
    "Food",
    "Transport",
    "Shopping",
    "Bills",
    "Entertainment",
    "Health",
    "Education",
    "Travel",
    "Other"
]


# ---------------------------------------------------
# INITIALIZE APP FILES
# ---------------------------------------------------

def initialize_app():

    # Create expenses.json
    if not os.path.exists(
        EXPENSES_FILE
    ):

        with open(
            EXPENSES_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                [],
                file,
                indent=4
            )

    # Create categories.json
    if not os.path.exists(
        CATEGORIES_FILE
    ):

        with open(
            CATEGORIES_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                DEFAULT_CATEGORIES,
                file,
                indent=4
            )

    # Create config.json
    if not os.path.exists(
        CONFIG_FILE
    ):

        with open(
            CONFIG_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                DEFAULT_SETTINGS,
                file,
                indent=4
            )


# ---------------------------------------------------
# CONFIG FUNCTIONS
# ---------------------------------------------------

def load_config():

    initialize_app()

    with open(
        CONFIG_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_config(config_data):

    with open(
        CONFIG_FILE,
        "w",
        encoding="utf-8"
    ) as file:

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