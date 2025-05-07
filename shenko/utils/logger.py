"""
Logger utility module for Shenko.

This module provides a structured logging system with timestamp and categorization,
making it easier to track and debug issues.
"""

import os
import sys
import logging
import traceback
from datetime import datetime

# Define log levels
LOG_LEVELS = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}

# Default configuration
DEFAULT_LOG_LEVEL = 'INFO'
DEFAULT_LOG_FILE = 'shenko_log.txt'
DEFAULT_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Initialize logger
logger = None

def setup_logger(log_file=DEFAULT_LOG_FILE, log_level=DEFAULT_LOG_LEVEL):
    """
    Set up the logger with the specified configuration.
    
    Args:
        log_file (str): Path to the log file.
        log_level (str): Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
        
    Returns:
        logging.Logger: The configured logger instance.
    """
    global logger
    
    # Get the log level
    level = LOG_LEVELS.get(log_level.upper(), logging.INFO)
    
    # Create logger
    logger = logging.getLogger('shenko')
    logger.setLevel(level)
    
    # Create file handler
    try:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        
        # Create formatter
        formatter = logging.Formatter(DEFAULT_FORMAT)
        file_handler.setFormatter(formatter)
        
        # Add handler to logger
        logger.addHandler(file_handler)
        
        # Optionally add console handler for development
        if os.environ.get('SHENKO_DEBUG', '0') == '1':
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
            
        logger.info("Logger initialized successfully")
    except Exception as e:
        print(f"Failed to set up logger: {e}")
    
    return logger

def get_logger():
    """
    Get the logger instance. Initialize it if it hasn't been initialized yet.
    
    Returns:
        logging.Logger: The logger instance.
    """
    global logger
    if logger is None:
        return setup_logger()
    return logger

def log_uncaught_exception(ex_cls, ex, tb):
    """
    Log uncaught exceptions with detailed traceback.
    
    Args:
        ex_cls: Exception class.
        ex: Exception instance.
        tb: Traceback object.
    """
    log = get_logger()
    log.critical(f"Uncaught {ex_cls.__name__}: {ex}")
    
    # Format traceback
    formatted_tb = "".join(traceback.format_tb(tb))
    log.critical(f"Traceback:\n{formatted_tb}")
    
    # Also log to separate file for serious errors
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    with open(f"crash_log_{timestamp}.txt", "w") as f:
        f.write(f"Exception: {ex_cls.__name__}: {ex}\n")
        f.write(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Traceback:\n{formatted_tb}")
        
    # Display to user if possible
    print(f"Critical error occurred: {ex}")
    print("See log files for details.")
