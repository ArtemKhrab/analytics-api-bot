from config.config import HOST

import requests
from requests import HTTPError


class LikeCreationHandler:
    def __init__(self, user, post):
        self.access_token = user["access_token"]
        self.post_id = post["id"]

    def handle_like_creation(self):
        self._handle_like_creation()

    def _handle_like_creation(self):
        request_url = f"{HOST}post/{self.post_id}/like"

        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        response = requests.put(
            url=request_url,
            headers=headers
        )

        if response.status_code != 204:
            raise HTTPError(response.text)
