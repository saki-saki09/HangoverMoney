import json
import os

CATEGORY_FILE = os.path.join("data", "categories.json")

def load_categories():
    """
    Load the list of valid expense categories from the JSON file.
    """
    try:
        with open(CATEGORY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    

def save_categories(categories):
    """
    Save the list of valid expense categories to the JSON file.
    """
    with open(CATEGORY_FILE, "w") as file:
        json.dump(categories, file, indent=4)
    
def add_category(category_name):
    """
    Add a new expense category.
    """

    categories = load_categories()

    category_name = category_name.strip().title()

    # Prevent Duplicates
    if category_name in categories:
        return False, "Category already exists."
    
    categories.append(category_name)

    save_categories(categories)

    return True, f"{category_name} added successfully."

def delete_category(category_name):
    """
    Delete an expense category.
    """
    categories = load_categories()
    category_name = category_name.strip().title()

    if category_name not in categories:
        return False, "Category not found."

    categories.remove(category_name)
    save_categories(categories)
    return True, f"{category_name} deleted successfully."