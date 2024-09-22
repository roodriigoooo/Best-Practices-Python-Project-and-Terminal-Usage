import logging
import json
import datetime
import threading

class CustomJsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.datetime.fromtimestamp(record.created).isoformat() + "Z",
            "thread": threading.current_thread().name,
            "logger_name": record.name,
            "level": record.levelname,
            "message": record.getMessage(),
            "function": record.funcName,
            "line": record.lineno,
        }
        return json.dumps(log_record)

def setup_logger(name, level=logging.INFO):
    """
    Set up a logger with console and JSON file handlers, including additional metadata.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Console handler with simple formatter
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter("%(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)

    # JSON file handler
    json_handler = logging.FileHandler("app_logs.json")
    json_formatter = CustomJsonFormatter()
    json_handler.setFormatter(json_formatter)

    # Clear existing handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(json_handler)

    return logger
