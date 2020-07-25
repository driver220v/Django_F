import logging


def create_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    foramtter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    file_handler = logging.FileHandler('scrape_data.log')
    file_handler.setFormatter(foramtter)
    logger.addHandler(file_handler)
    return logger


logger = create_logger()