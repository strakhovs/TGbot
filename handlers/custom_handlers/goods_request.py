import json
import requests
import config_data.config

url = "https://aliexpress-datahub.p.rapidapi.com/item_search_2"
headers = {
        "X-RapidAPI-Key": config_data.config.RAPID_API_KEY,
        "X-RapidAPI-Host": "aliexpress-datahub.p.rapidapi.com"
    }


def make_request(query: str, asc=True, start_price="1", end_price=None) -> list:
    """
    Создаёт запрос к API, возвращает список товаров
    """
    querystring = {"q": query, "sort": "priceAsc" if asc else "priceDes",
                   "startPrice": start_price, "endPrice": end_price,
                   "locale": "ru_RU", "region": "RU", "currency": "RUB"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code == 200:
        raw_data = json.loads(response.text)
        data = raw_data["result"]["resultList"]
        return data
    else:
        return []
