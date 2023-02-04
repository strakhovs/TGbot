from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def url_button(url: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Перейти', url=url))
    return keyboard
