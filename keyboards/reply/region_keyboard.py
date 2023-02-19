from telebot.types import ReplyKeyboardMarkup, KeyboardButton


regions = ['RU', 'US', 'ES', 'FR', 'UK', 'BR', 'IL', 'NL', 'CA', 'IT', 'CL', 'UA', 'PL', 'AU', 'DE', 'BE']
currencies = ['RUB', 'USD', 'EUR', 'CAD', 'CHF', 'AUD', 'SGD', 'KRW', 'JPY', 'PLN', 'GBP', 'SEK', 'NZD']


def region_keyboard() -> ReplyKeyboardMarkup:
    """
    Клавиатура со списком регионов
    """
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for region in regions:
        keyboard.add(KeyboardButton(text=region))
    return keyboard


def currency_keyboard() -> ReplyKeyboardMarkup:
    """
    Клавиатура со списком валют
    """
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for currency in currencies:
        keyboard.add(KeyboardButton(text=currency))
    return keyboard
