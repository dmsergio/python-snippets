# logging_test.py
from logging_handler_config import get_logger

_logger = get_logger()

if __name__ == '__main__':
    _logger.debug("Debug message")
    _logger.info("Info message")
    _logger.warning("Warning message")
    _logger.error("Error message")
    _logger.critical("Critical message")
