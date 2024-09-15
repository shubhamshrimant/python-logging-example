# import logging
# logger = logging.getLogger('shared_logger')

# logger.setLevel(logging.DEBUG)

# file_handler = logging.FileHandler('shared_file.log')
# file_handler.setLevel(logging.DEBUG)

# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)
# logging_config.py

import logging

# Create or get the logger
logger = logging.getLogger('shared_logger')
logger.setLevel(logging.DEBUG)  # Log everything (DEBUG level or higher)

# Prevent multiple handlers if the logger is configured multiple times
if not logger.handlers:
    # Create a file handler to log to a file
    file_handler = logging.FileHandler('shared_log_file.log')
    file_handler.setLevel(logging.DEBUG)

    # Define log format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add file handler to logger
    logger.addHandler(file_handler)
