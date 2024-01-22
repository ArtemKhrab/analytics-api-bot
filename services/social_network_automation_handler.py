import logging
import random
import traceback
import pickle

from config.config import LOGGER_NAME
from config.config import NUMBER_OF_USERS
from config.config import MAX_POSTS_PER_USER
from config.config import MAX_LIKES_PER_USER
from config.config import USERS_FILE_NAME

from services.user_register_handler import UserRegisterHandler
from services.post_creation_handler import PostCreationHandler
from services.like_creation_handler import LikeCreationHandler
from services.posts_scraper import PostScraper


logger = logging.getLogger(LOGGER_NAME)


class SocialNetworkAutomationHandler:
    def handle_social_network_automation(self):
        users = self._create_users()
        self._save_users(
            users=users
        )
        self._create_posts(users)

        try:
            posts = PostScraper().scrape_posts()
        except Exception as exc:
            self._handle_exception(exc)
            return

        self._create_likes(users, posts)

    def _create_users(self):
        users = []
        for _ in range(NUMBER_OF_USERS):
            try:
                user_data = UserRegisterHandler().handle_user_registration()
                users.append(user_data)
            except Exception as exc:
                self._handle_exception(exc)
        return users

    def _create_posts(self, users):
        for user in users:
            self._create_post(user)

    def _create_likes(self, users, posts):
        for user in users:
            self._create_like(user, posts)

    def _create_post(self, user):
        for _ in range(random.randint(1, MAX_POSTS_PER_USER)):
            try:
                PostCreationHandler(user).handle_post_creation()
            except Exception as exc:
                self._handle_exception(exc)

    def _create_like(self, user, posts):
        random_posts = [random.choice(posts) for _ in range(random.randint(1, MAX_LIKES_PER_USER))]

        for post in random_posts:
            try:
                LikeCreationHandler(user, post).handle_like_creation()
            except Exception as exc:
                self._handle_exception(exc)

    @staticmethod
    def _save_users(users):
        with open(USERS_FILE_NAME, "wb") as fp:
            pickle.dump(users, fp)

    @staticmethod
    def _handle_exception(exc):
        error_msg = f"Error occurred: {exc} | {traceback.format_exc()}"
        logger.error(error_msg)
