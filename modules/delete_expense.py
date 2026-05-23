from utils.storage import load_data, save_data
from utils.logger import (
    log_info,
    log_error
)

def delete_expense(expense_id):
    """
    Delete expense by ID safely.
    """

    try:
        data = load_data()
        
        updated_data = [
            expense for expense in data
            if expense["id"] != expense_id
        ]

        if len(updated_data) == len(data):
            return False, "Expense not found."
        
        save_data(updated_data)
        log_info(f"Expense - {expense_id}\nDeleted successfully.")

        return True, "Expense deleted successfully."
    except Exception as error:
        log_error(f"Delete Expense Error: {error}")

        return False, str(error)
    
    
        