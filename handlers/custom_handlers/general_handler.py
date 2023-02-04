from telebot.types import Message
from telebot import custom_filters
from loader import bot
from states.custom_states import MyStates
from keyboards.inline.url_button import url_button


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
