import requests
from requests import Response


class RequestService:

    @staticmethod
    def get(url: str, params: str, verify: str=None) -> Response:
        return requests.get(url=url, params=params, verify=verify)
