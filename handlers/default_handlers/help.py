from loguru import logger
from telebot.types import Message
from config_data.config import DEFAULT_COMMANDS
from loader import bot


@bot.message_handler(commands=["help"])
def bot_help(message: Message) -> None:
    """
    Обработка команды /help
    """
    logger.debug(f'Вызвана команда /help, пользователь: {message.from_user.id}')
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message, "\n".join(text))
