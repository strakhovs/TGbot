from telebot.types import Message
from loader import bot
from states.custom_states import MyStates
from .goods_request import make_request


@bot.message_handler(commands=["high"])
def high_command(message: Message) -> None:
    """
    Обработка команды /high
    """
    bot.set_state(message.from_user.id, MyStates.search_high, message.chat.id)
    bot.send_message(message.chat.id, "Введите строку для поиска")


@bot.message_handler(state=MyStates.search_high)
def get_search_result(message: Message) -> None:
    """
    Получение результатов поиска, запрос количества отображаемых элементов
    """
    bot.set_state(message.from_user.id, MyStates.search_layout, message.chat.id)
    try:
        bot.response = make_request(message.text, asc=False)
    except Exception:
        bot.send_message(message.chat.id, "Ничего не найдено")
        bot.delete_state(message.from_user.id)
    else:
        bot.send_message(message.chat.id, "Сколько товаров отображать?\n(Максимум - 20)")
