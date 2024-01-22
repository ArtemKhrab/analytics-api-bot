from config.config import HOST

import requests
from requests import HTTPError


class PostScraper:
    @staticmethod
    def scrape_posts():
        request_url = f"{HOST}post/"
        response = requests.get(
            url=request_url,
        )

        if response.status_code != 200:
            raise HTTPError(response.text)

        return response.json()
