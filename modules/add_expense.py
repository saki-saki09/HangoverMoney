import uuid

from utils.storage import load_data, save_data
from utils.helpers import get_current_date
from utils.validators import (validate_amount, validate_category, validate_note)
from utils.logger import log_info


def add_expense(amount, category, note=""):
    """
    Add a new valid expense into the storage...
    """
    # Validate amount
    valid_amount, amount_result = validate_amount(amount)
    
    if not valid_amount:
        return False, amount_result
    
    # Validate category
    valid_category, category_result = validate_category(category)

    if not valid_category:
        return False, category_result

    # Validate note
    valid_note, note_result = validate_note(note)

    if not valid_note:
        return False, note_result

    data = load_data()
    
    expense = {
        "id": str(uuid.uuid4()),
        "amount": amount_result,
        "category": category_result,
        "note": note_result,
        "date": get_current_date()
    }

    data.append(expense)

    save_data(data)
    log_info(f"Expense added: {category_result} - {amount_result}")

    return True, expense

