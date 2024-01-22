from config.config import HOST

from utils.utils import post_text_generator

import requests
from requests import HTTPError


class PostCreationHandler:
    def __init__(self, user_data):
        self.access_token = user_data["access_token"]

    def handle_post_creation(self):
        post_text = post_text_generator()
        self._handle_post_creation(
            post_text=post_text
        )

    def _handle_post_creation(self, post_text):
        request_url = f"{HOST}post/"

        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        request_data = {
            "text": post_text,
        }

        response = requests.post(
            url=request_url,
            data=request_data,
            headers=headers
        )

        if response.status_code != 201:
            raise HTTPError(response.text)
