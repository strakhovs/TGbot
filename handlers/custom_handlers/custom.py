from loguru import logger
from telebot.types import Message

from database.CRUD import store_message
from loader import bot
from states.custom_states import MyStates
from .goods_request import make_request


@bot.message_handler(commands=["custom"])
def custom_command(message: Message) -> None:
    """
    Обработка команды /custom
    """
    logger.debug('Вызвана команда /custom')
    bot.set_state(message.from_user.id, MyStates.search_custom_start, message.chat.id)
    bot.send_message(message.chat.id, "Введите строку для поиска")


@bot.message_handler(state=MyStates.search_custom_start)
def get_custom_start(message: Message) -> None:
    store_message(message)
    bot.set_state(message.from_user.id, MyStates.search_custom_end, message.chat.id)
    bot.query = message.text
    bot.send_message(message.chat.id, "Введите начальную цену")


@bot.message_handler(state=MyStates.search_custom_end)
def get_custom_end(message: Message) -> None:
    store_message(message)
    if message.text.isdigit():
        bot.set_state(message.from_user.id, MyStates.search_custom, message.chat.id)
        bot.start_price = message.text
        bot.send_message(message.chat.id, "Введите конечную цену")
    else:
        bot.send_message(message.chat.id, "Введите число")


@bot.message_handler(state=MyStates.search_custom)
def get_search_result(message: Message) -> None:
    """
    Получение результатов поиска, запрос количества отображаемых элементов
    """
    store_message(message)
    if message.text.isdigit():
        bot.set_state(message.from_user.id, MyStates.search_layout, message.chat.id)
        bot.end_price = message.text
        try:
            bot.response = make_request(bot.query, start_price=bot.start_price, end_price=bot.end_price)
        except Exception as exc:
            logger.exception(f'Запрос не дал результатов, {exc}')
            bot.send_message(message.chat.id, "Ничего не найдено. Проверьте ввод")
            bot.delete_state(message.from_user.id)
        else:
            bot.send_message(message.chat.id, "Сколько товаров отображать?\n(Максимум - 20)")
    else:
        bot.send_message(message.chat.id, "Введите число")
