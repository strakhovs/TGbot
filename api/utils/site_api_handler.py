from typing import Dict, Union
import requests


def _make_response(method: str, url: str, headers: Dict, params: Dict, timeout: int, success=200):

    response = requests.request(
        method,
        url,
        headers=headers,
        params=params,
        timeout=timeout
    )
    status_code = response.status_code
    if status_code == success:
        return response
    else:
        return status_code


def _get_low_price(method: str, url: str, headers: Dict, params: Dict, timeout: int, func=_make_response):
    response = func(method, url, headers=headers, params=params, timeout=timeout)
    return response


class SiteApiInterface:
    @staticmethod
    def get_low_prices():
        return _get_low_price

