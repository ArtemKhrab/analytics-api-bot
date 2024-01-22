from datetime import datetime

# Logging config
LOGGER_FILE_NAME_FORMAT = "logger.log"
LOGGER_NAME = "social_network_api_automation"
LOGGER_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOGGER_MAX_LOG_FILES = 7
LOGGER_LOGS_FOLDER = "logs"

# Automation config
NUMBER_OF_USERS = 3
MAX_POSTS_PER_USER = 4
MAX_LIKES_PER_USER = 15

PASSWORD_LENGTH = 10

USERS_FILE_NAME = f"users_dump_{int(datetime.timestamp(datetime.utcnow()))}"

# API config
API_VERSION = "v1"
HOST = f"http://127.0.0.1:8000/api/{API_VERSION}/"

# Post config
POST_TEMPLATE_TEXT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
