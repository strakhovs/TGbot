from telebot.types import Message
from loguru import logger
from database.CRUD import get_history
from loader import bot


@bot.message_handler(commands=["history"])
def history_command(message: Message) -> None:
    """
    Обработка команды /history
    """
    logger.debug(f'Вызвана команда /history, пользователь: {message.from_user.id}')
    responses = get_history(int(message.from_user.id))
    if responses:
        for item in responses:
            response_list = eval(item['response'])
            for response in response_list:
                bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, 'История пуста')
