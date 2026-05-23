import json
import os

from utils.config import (
    EXPENSES_FILE
)


# ----------------------------------------
# CREATE FILE IF MISSING
# ----------------------------------------

def initialize_storage():

    if not os.path.exists(EXPENSES_FILE):

        with open(EXPENSES_FILE, "w") as file:

            json.dump([], file)


# ----------------------------------------
# LOAD DATA
# ----------------------------------------

def load_data():

    initialize_storage()

    try:

        with open(EXPENSES_FILE, "r") as file:

            return json.load(file)

    except:

        return []


# ----------------------------------------
# SAVE DATA
# ----------------------------------------

def save_data(data):

    with open(EXPENSES_FILE, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )