from telebot.types import Message
from loader import bot
from states.custom_states import MyStates
from .goods_request import make_request


@bot.message_handler(commands=["custom"])
def custom_command(message: Message) -> None:
    """
    Обработка команды /custom
    """
    bot.set_state(message.from_user.id, MyStates.search_custom_start, message.chat.id)  # Состояние MyStates.search
    bot.send_message(message.chat.id, "Введите строку для поиска")


@bot.message_handler(state=MyStates.search_custom_start)
def get_custom_start(message: Message) -> None:
    bot.set_state(message.from_user.id, MyStates.search_custom_end, message.chat.id)
    bot.query = message.text
    bot.send_message(message.chat.id, "Введите начальную цену")


@bot.message_handler(state=MyStates.search_custom_end)
def get_custom_end(message: Message) -> None:
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
    if message.text.isdigit():
        bot.set_state(message.from_user.id, MyStates.search_layout, message.chat.id)
        bot.end_price = message.text
        bot.response = make_request(bot.query, start_price=bot.start_price, end_price=bot.end_price)
        bot.send_message(message.chat.id, "Сколько товаров отображать?\n(Максимум - 20)")
    else:
        bot.send_message(message.chat.id, "Введите число")