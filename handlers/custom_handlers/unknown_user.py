from telebot.types import Message

from loader import bot
from states.custom_states import MyStates


def user_registration(message: Message) -> None:
    """
    Переход к регистрации пользователя, запрос имени
    """
    bot.send_message(message.chat.id, "Кажется, мы не знакомы.\nКак я могу Вас называть?")
    bot.set_state(message.from_user.id, MyStates.registration_name, message.chat.id)
