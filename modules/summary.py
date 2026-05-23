from utils.storage import load_data
from utils.logger import log_error

def get_total_expenses():
    """
    Calculate the total amount of all expenses.
    """
    try:
        data = load_data()

        total = sum(
            item["amount"]
            for item in data
        )

        return True, total
    except Exception as error:
        log_error(f"Summary Error: {error}")
        return False, str(error)


def category_summary():
    """
    Provide a summary of expenses by category.
    """
    try:
        data = load_data()

        summary = {}

        for item in data:
            category = item["category"]
            summary[category] = (
                summary.get(category, 0)
                + item["amount"]
            )
        
        return True, summary
    
    except Exception as error:
        log_error(f"Category Summary Error: {error}")
        return False, str(error)
    

