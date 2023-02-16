from telebot.types import Message
from loguru import logger
from database.CRUD import store_message
from loader import bot
from states.custom_states import MyStates
from .goods_request import make_request


@bot.message_handler(commands=["low"])
def low_command(message: Message) -> None:
    """
    Обработка команды /low
    """
    logger.debug(f'Вызвана команда /low, пользователь: {message.from_user.id}')
    bot.set_state(message.from_user.id, MyStates.search_low, message.chat.id)
    bot.send_message(message.chat.id, "Введите строку для поиска")


@bot.message_handler(state=MyStates.search_low)
def get_search_result(message: Message) -> None:
    """
    Получение результатов поиска, запрос количества отображаемых элементов
    """
    store_message(message)
    bot.set_state(message.from_user.id, MyStates.search_layout, message.chat.id)
    try:
        bot.response = make_request(message.text)
    except Exception as exc:
        logger.exception(f'Запрос не дал результатов, {exc}')
        bot.send_message(message.chat.id, "Ничего не найдено. Проверьте ввод")
        bot.delete_state(message.from_user.id)
    else:
        bot.send_message(message.chat.id, "Сколько товаров отображать?\n(Максимум - 20)")
