from loguru import logger
from telebot.types import Message
from loader import bot
from database.models import User
from states.custom_states import MyStates


@bot.message_handler(commands=["start"])
def bot_start(message: Message) -> None:
    """
    Обработка команды /start
    """
    logger.debug(f'Вызвана команда /start, пользователь: {message.from_user.id}')
    try:
        user = User.get(User.person_id == message.from_user.id)
    except User.DoesNotExist:
        bot.send_message(message.chat.id, "Кажется, мы не знакомы.\nКак я могу Вас называть?")
        bot.set_state(message.from_user.id, MyStates.registration_name, message.chat.id)
    else:
        bot.reply_to(message, f"Привет, {user.name}!")
