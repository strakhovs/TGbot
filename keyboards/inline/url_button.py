from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def url_button(url: str) -> InlineKeyboardMarkup:
    """
    Кнопка перехода по url товара
    """
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Перейти', url=url))
    return keyboard
