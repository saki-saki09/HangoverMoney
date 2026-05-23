from modules.category_manager import load_categories

def validate_amount(amount):
    """
    Validate expense amount.
    """

    try:
        amount = float(amount)

        if amount <= 0:
            return False, "Amount must be greater than 0."

        return True, amount

    except ValueError:
        return False, "Amount must be a number."


def validate_category(category):
    """
    Validate category field.
    """
    category = category.strip().title()

    if not category:
        return False, "Category cannot be empty."
    
    categories = load_categories()

    if category not in categories:
        return False, "Invalid category."

    return True, category


def validate_note(note):
    """
    Validate note field.
    """

    return True, note.strip()