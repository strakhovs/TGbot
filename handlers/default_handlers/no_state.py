from loguru import logger
from telebot.types import Message
from loader import bot
from database.CRUD import store_message


@bot.message_handler(state=None)
def bot_reply(message: Message) -> None:
    """
    Обработка сообщений без указанного состояния
    """
    logger.debug(f'Отправлено сообщение без указанного состояния. {message.from_user.id}: {message.text}')
    store_message(message)
    bot.reply_to(
        message, "Я Вас не понимаю.\nДля справки вызовите команду /help"
    )
