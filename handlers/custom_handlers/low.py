from telebot.types import Message
from telebot import custom_filters

from keyboards.inline.url_button import url_button
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
    Получение результатов поиска, запрос количества отображаемых элементов
    """
    bot.set_state(message.from_user.id, MyStates.search_layout, message.chat.id)
    bot.response = make_request(message.text)
    bot.send_message(message.chat.id, "Сколько товаров отображать?\n(Максимум - 20)")


@bot.message_handler(state=MyStates.search_layout)
def get_result_layout(message: Message) -> None:
    """
    Вывод результатов поиска
    """
    if message.text.isdigit() and 0 < int(message.text) < 21:
        if bot.response:
            counter = 1
            for item in bot.response:
                bot.send_photo(message.chat.id, f'http:{item["item"]["image"]}')
                bot.send_message(message.chat.id,
                                 f'{item["item"]["title"]}\n'
                                 f'{item["item"]["sku"]["def"]["promotionPrice"]} руб.\n',
                                 reply_markup=url_button(f'https:{item["item"]["itemUrl"]}'))
                if counter == int(message.text):
                    break
                counter += 1
        else:
            bot.send_message(message.chat.id, "Что-то пошло не так")
        bot.delete_state(message.from_user.id, message.chat.id)  # Сброс состояния
    else:
        bot.send_message(message.chat.id, "Введите число от 1 до 20")


bot.add_custom_filter(custom_filters.StateFilter(bot))
