import os

from config.config import LOGGER_LOGS_FOLDER
from services.social_network_automation_handler import SocialNetworkAutomationHandler
from utils.utils import configure_logger


if not os.path.exists(LOGGER_LOGS_FOLDER):
    os.mkdir(LOGGER_LOGS_FOLDER)

configure_logger()


def main():
    SocialNetworkAutomationHandler().handle_social_network_automation()


if __name__ == "__main__":
    main()
