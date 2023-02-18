from telebot.types import ReplyKeyboardMarkup, KeyboardButton


regions = ['US', 'RU', 'ES', 'FR', 'UK', 'BR', 'IL', 'NL', 'CA', 'IT', 'CL', 'UA', 'PL', 'AU', 'DE', 'BE']
currencies = ['USD', 'EUR', 'CAD', 'CHF', 'AUD', 'SGD', 'KRW', 'JPY', 'PLN', 'GBP', 'SEK', 'NZD', 'RUB']


def region_keyboard():
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for region in regions:
        keyboard.add(KeyboardButton(text=region))
    return keyboard


def currency_keyboard():
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for currency in currencies:
        keyboard.add(KeyboardButton(text=currency))
    return keyboard
