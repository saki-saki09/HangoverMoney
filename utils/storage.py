import json
import os
import shutil

from utils.logger import (
    log_info,
    log_error
)

DATA_FOLDER = "data"


# Path to JSON file...
DATA_FILE = os.path.join(DATA_FOLDER, "expenses.json")

BACKUP_FILE = os.path.join(DATA_FOLDER, "expenses_backup.json")

def initialize_storage():
    """
    Create data folder and JSON file if missing
    """

    #Create data folder
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)
    
    #Create expenses.json if missing
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            json.dump([], file, indent=4)

def create_backup():
    """
    Create backup of the current data
    """

    if os.path.exists(DATA_FILE):
        shutil.copy(DATA_FILE, BACKUP_FILE)


def load_data():
    """
    Load data safely...
    """

    initialize_storage()

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    
    except json.JSONDecodeError:
        # Try backup recovery...
        if os.path.exists(BACKUP_FILE):
            with open(BACKUP_FILE, "r") as file:
                return json.load(file)
            log_error("Main JSON file is corrupted. Backup recovery used.")
        
        return []


def save_data(data):
    """
    Save expenses safely...
    """

    initialize_storage()

    #Create backup before overwrite...
    create_backup()

    temp_file = DATA_FILE + ".tmp"

    try:

        #Write into temporary file first...
        with open(temp_file, "w") as file:
            json.dump(data, file, indent=4)
        
        # Replace original safely...
        os.replace(temp_file, DATA_FILE)

        log_info("Expenses saved successfully.")

    except Exception as error:
        log_error(f"Save Error: {error}")

        if os.path.exists(temp_file):
            os.remove(temp_file)