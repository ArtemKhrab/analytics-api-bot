from config.config import HOST

from utils.utils import username_generator
from utils.utils import password_generator

import requests
from requests import HTTPError


class UserRegisterHandler:

    def handle_user_registration(self):
        username = username_generator()
        password = password_generator()
        tokens = self._handle_user_registration(
            username=username,
            password=password
        )

        return {
            "username": username,
            "password": password,
            "access_token": tokens["access"]
        }

    @staticmethod
    def _handle_user_registration(username, password):
        request_url = f"{HOST}register/"

        request_data = {
            "username": username,
            "password": password
        }

        response = requests.post(
            url=request_url,
            data=request_data
        )

        if response.status_code != 200:
            raise HTTPError(response.text)

        return response.json()
