import json
import os

CONFIG_FOLDER = "data"

CONFIG_FILE = os.path.join(CONFIG_FOLDER, "config.json")

DEFAULT_CONFIG = {
    "currency": "BDT",
    "theme": "dark",
    "window_width": 1000,
    "window_height": 600,
    "default_category": "Food",
    "date_format": "%Y-%m-%d"
}

def initialize_config():
    """
    Create config file if missing
    """

    if not os.path.exists(CONFIG_FILE):

        with open(CONFIG_FILE, "w") as file:
            json.dump(DEFAULT_CONFIG, file, indent=4)


def load_config():
    """
    Load configuration safely...
    """

    initialize_config()

    try:
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return DEFAULT_CONFIG
    

def save_config(config_data):
    """
    Save configuration...
    """
    with open(CONFIG_FILE, "w") as file:
        json.dump(config_data, file, indent=4)


def get_setting(key):
    """
    Get single config value...
    """
    config = load_config()

    return config.get(key)

def update_setting(key, value):
    """
    Update single config value...
    """

    config = load_config()

    config[key] = value

    save_config(config)