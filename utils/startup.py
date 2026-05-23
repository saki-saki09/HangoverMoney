from utils.storage import initialize_storage
from utils.config import initialize_config

from utils.logger import log_info

def initialize_app():
    """
    Initialize the application safely...
    """
    initialize_storage()
    initialize_config()
    log_info("Application started successfully.")
    