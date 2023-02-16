from loguru import logger
from telebot.types import Message
from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    logger.debug(f'Вызвана команда /start, пользователь: {message.from_user.id}')
    bot.reply_to(message, f"Привет, {message.from_user.full_name}!")
