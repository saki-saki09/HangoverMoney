import os
import sys

from datetime import datetime
from utils.constants import DATE_TIME_FORMAT

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(
        base_path,
        relative_path
    )

def get_current_date():
    """
    Return current date in DD-MM-YYYY format...
    """
    return datetime.now().strftime(DATE_TIME_FORMAT)

def format_currency(amount):
    """
    Format number as currency string...
    Example: 1000 -> '৳-1000'
    """
    return f"৳-{amount}"

