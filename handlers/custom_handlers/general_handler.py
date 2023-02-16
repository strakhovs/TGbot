from telebot.types import Message
from telebot import custom_filters

from database.CRUD import store_message, store_response
from loader import bot
from states.custom_states import MyStates
from keyboards.inline.url_button import url_button


@bot.message_handler(state=MyStates.search_layout)
def get_result_layout(message: Message) -> None:
    """
    Вывод результатов поиска
    """
    currencies_symbols = {'USD': '$',
                          'EUR': '€',
                          'CAD': '$',
                          'CHF': '₣',
                          'AUD': '$',
                          'SGD': '$',
                          'KRW': '₩',
                          'JPY': '¥',
                          'PLN': 'zł',
                          'GBP': '£',
                          'SEK': 'kr',
                          'NZD': '$',
                          'RUB': '₽'}

    store_message(message)
    if message.text.isdigit() and 0 < int(message.text) < 21:
        if bot.response:
            result_list = []
            counter = 1
            for item in bot.response:
                bot.send_photo(message.chat.id, f'http:{item["item"]["image"]}')
                result = f'{item["item"]["title"]}\n' \
                         f'⭐: {item["item"]["averageStarRate"] if item["item"]["averageStarRate"] else "-"}\n' \
                         f'{item["item"]["sku"]["def"]["promotionPrice"]} ' \
                         f'{currencies_symbols[bot.current_user.currency]}\n'
                bot.send_message(message.chat.id, result, reply_markup=url_button(f'https:{item["item"]["itemUrl"]}'))
                result = f'http:{item["item"]["image"]}|' + result + f'|https:{item["item"]["itemUrl"]}'
                result_list.append(result)
                if counter == int(message.text):
                    break
                counter += 1
            store_response(int(message.from_user.id), str(result_list))
        else:
            bot.send_message(message.chat.id, "Что-то пошло не так")
        bot.delete_state(message.from_user.id, message.chat.id)  # Сброс состояния
    else:
        bot.send_message(message.chat.id, "Введите число от 1 до 20")


bot.add_custom_filter(custom_filters.StateFilter(bot))
