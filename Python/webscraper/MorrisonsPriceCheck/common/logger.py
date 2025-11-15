import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
    #filename='my_script.log',               # Log file name
    format="{asctime} - {levelname:<9} - {name} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
    level=logging.INFO
)

def log_to_file(message: str, log_level: str):
    if log_level == "DEBUG":
        logger.debug(message)
    elif log_level == "INFO":
        logger.info(message)
    elif log_level == "WARNING":
        logger.warning(message)
    elif log_level == "ERROR":
        logger.error(message)
    elif log_level == "CRITICAL":
        logger.critical(message)

if __name__ == "__main__":
    log_to_file("This is a warning", "WARNING")
    log_to_file("This is an info", "INFO")
    log_to_file("This is critical", "CRITICAL")
    log_to_file("This is error", "ERROR")
    log_to_file("This is debug", "DEBUG")
