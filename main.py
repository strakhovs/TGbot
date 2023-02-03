from bot.core import bot
from api.core import headers, querystring, site_api, url
"""
Главный скрипт, запускающий бота.
"""
# bot.infinity_polling()
# querystring = {"q": "телефон", "page": "1", "sort": "priceAsc", "currency": "RUB"}

low_prices = site_api.get_low_prices()
response = low_prices("GET", url, headers, querystring, timeout=3)
print(response.text)
