from loguru import logger
from telebot.types import Message

from database.CRUD import store_message
from loader import bot
from states.custom_states import MyStates
from .goods_request import make_request


@bot.message_handler(commands=["edit"])
def edit_command(message: Message) -> None:
    """
    Обработка команды /edit
    """
    bot.set_state(message.from_user.id, MyStates.registration_name, message.chat.id)
    bot.send_message(message.chat.id, "Как мне Вас называть?")
