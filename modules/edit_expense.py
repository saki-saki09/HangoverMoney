from utils.storage import load_data, save_data
from utils.logger import (
    log_error,
    log_info
)
from utils.validators import (
    validate_amount,
    validate_category,
    validate_note
)

def edit_expense(expense_id, new_amount, new_category, new_note):
    """
    Edit an existing expense using its ID safely.
    """

    try:

        # Validate amount
        valid_amount, amount_result = validate_amount(new_amount)

        if not valid_amount:
            return False, amount_result
        
        # Validate category
        valid_category, category_result = validate_category(new_category)

        if not valid_category:
            return False, category_result
        
        # Validate Note...
        _, note_result = validate_note(new_note)

        data = load_data()

        for expense in data:

            if expense["id"] == expense_id:

                expense["amount"] = amount_result
                expense["category"] = category_result
                expense["note"] = note_result

                save_data(data)

                log_info(
                    f"Expense updated successfully: {expense_id}"
                )

                return True, expense
            
        return False, "Expense not found"
    except Exception as error:
        log_error(f"Edit Expense Error: {error}")

        return False, str(error)
    
