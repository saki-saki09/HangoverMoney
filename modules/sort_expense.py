from utils.storage import load_data

def sort_expenses(sort_by="date", descending=True):
    """
    Sort expenses based on selected field...
    """

    expenses = load_data()

    #Valid sorting fields...
    valid_fields = ["date", "amount", "category"]

    if sort_by not in valid_fields:
        return False, "Invalid sorting field."
    
    try:
        sorted_expenses = sorted(expenses, key=lambda expense: expense[sort_by], reverse=descending)

        return True, sorted_expenses
    except Exception as error:
        return False, str(error)
    