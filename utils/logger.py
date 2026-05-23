import logging
import os

# Create logs folder if missing...
if not os.path.exists("logs"):
    os.makedirs("logs")

LOG_FOLDER = "logs"
LOG_FILE = os.path.join(LOG_FOLDER, "app.log")


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