from utils.storage import load_data
from utils.logger import log_error


def get_all_expenses():
    """
    Return all expenses safely...
    """
    
    try:
        data = load_data()

        return True, data
    
    except Exception as error:
        log_error(f"View Expense Error: {error}")

        return False, str(error)


def get_expense_by_id(expense_id):
    """
    Find single expense by ID.
    """

    try:
        data = load_data()

        for expense in data:

            if expense["id"] == expense_id:
                return True, expense
        
        return False, "Expense not found."
    
    except Exception as error:

        log_error(f"Get Expense Error: {error}")

        return False, str(error)
    