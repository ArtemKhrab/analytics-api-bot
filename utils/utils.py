import uuid
import random
import string
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

from config.config import LOGGER_NAME
from config.config import LOGGER_FORMAT
from config.config import LOGGER_LOGS_FOLDER
from config.config import LOGGER_MAX_LOG_FILES
from config.config import LOGGER_FILE_NAME_FORMAT
from config.config import PASSWORD_LENGTH
from config.config import POST_TEMPLATE_TEXT


def configure_logger():
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG)

    log_file_name = datetime.now().strftime(
        f"{LOGGER_LOGS_FOLDER}/{LOGGER_FILE_NAME_FORMAT}"
    )

    handler = TimedRotatingFileHandler(
        log_file_name, when="midnight", interval=1, backupCount=LOGGER_MAX_LOG_FILES
    )
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(LOGGER_FORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def username_generator():
    return str(uuid.uuid4())


def password_generator():
    return "".join(random.choice(string.ascii_letters+string.digits) for _ in range(PASSWORD_LENGTH))


def post_text_generator():
    keys = POST_TEMPLATE_TEXT.split(" ")
    post_text = " ".join(random.choice(keys) for _ in range(random.randint(20, 100)))
    return post_text
