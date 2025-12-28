import logging
import os
import sys

class Logger:
    """Custom logger for the framework."""
    
    _logger = None

    @classmethod
    def get_logger(cls):
        if cls._logger:
            return cls._logger
            
        # Create logger
        logger = logging.getLogger("DigitalIdentityQA")
        logger.setLevel(logging.DEBUG)
        
        # Create handlers
        c_handler = logging.StreamHandler(sys.stdout)
        f_handler = logging.FileHandler('automation.log')
        c_handler.setLevel(logging.INFO)
        f_handler.setLevel(logging.DEBUG)
        
        # Create formatters and add it to handlers
        c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)
        
        # Add handlers to the logger
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)
        
        cls._logger = logger
        return cls._logger

log = Logger.get_logger()
