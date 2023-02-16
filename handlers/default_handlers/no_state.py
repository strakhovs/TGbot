from loguru import logger
from telebot.types import Message
from loader import bot
from database.CRUD import store_message

# Эхо хендлер, куда летят текстовые сообщения без указанного состояния


@bot.message_handler(state=None)
def bot_reply(message: Message):
    logger.debug(f'Отправлено сообщение без указанного состояния. {message.from_user.id}: {message.text}')
    store_message(message)
    bot.reply_to(
        message, "Я Вас не понимаю.\nДля вызова справки вызовите команду /help"
    )
