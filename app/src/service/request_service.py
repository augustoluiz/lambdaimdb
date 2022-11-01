import requests
from requests import Response


class RequestService:

    @staticmethod
    def get(url: str, headers: dict, verify: str=None) -> Response:
        return requests.get(url=url, headers=headers, verify=verify)
