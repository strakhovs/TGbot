from telebot.types import Message
from telebot import custom_filters
from loader import bot
from .goods_request import make_request
from states.custom_states import MyStates


@bot.message_handler(commands=["low"])
def low_command(message: Message) -> None:
    """
    Обработка команды /low
    """
    bot.set_state(message.from_user.id, MyStates.search, message.chat.id)  # Состояние MyStates.search
    bot.send_message(message.chat.id, "Введите строку для поиска")


@bot.message_handler(state=MyStates.search)
def get_search_result(message: Message) -> None:
    """
    Вывод результатов поиска
    """
    response = make_request(message.text)
    if response:
        for item in response:
            bot.send_photo(message.chat.id, f'http:{item["item"]["image"]}')
            bot.send_message(message.chat.id,
                             f'{item["item"]["title"]}\n'
                             f'{item["item"]["sku"]["def"]["promotionPrice"]} руб.\n'
                             f'https:{item["item"]["itemUrl"]}')
    else:
        bot.send_message(message.chat.id, "Что-то пошло не так")
    bot.delete_state(message.from_user.id, message.chat.id)  # Сброс состояния


bot.add_custom_filter(custom_filters.StateFilter(bot))
