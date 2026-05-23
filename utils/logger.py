import logging
import os
from utils.config import LOG_FILE

# Create logs folder if missing...
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Configure logging...
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(message):
    """
    Log info message...
    """
    logging.info(message)

def log_warning(message):
    """
    Log warning message...
    """
    logging.warning(message)

def log_error(message):
    """
    Log error message...
    """
    logging.error(message)