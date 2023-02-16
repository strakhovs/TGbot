from loguru import logger
from telebot.types import Message

from loader import bot
from states.custom_states import MyStates


@bot.message_handler(commands=["edit"])
def edit_command(message: Message) -> None:
    """
    Обработка команды /edit
    """
    logger.debug(f'Запущена команда /edit, пользователь: {message.from_user.id}')
    bot.set_state(message.from_user.id, MyStates.registration_name, message.chat.id)
    bot.send_message(message.chat.id, "Как мне Вас называть?")
