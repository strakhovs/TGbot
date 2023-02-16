from telebot.types import Message
from loguru import logger
from database.CRUD import store_message
from database.models import User
from loader import bot
from states.custom_states import MyStates


regions = ['US', 'RU', 'ES', 'FR', 'UK', 'BR', 'IL', 'NL', 'CA', 'IT', 'CL', 'UA', 'PL', 'AU', 'DE', 'BE']
currencies = ['USD', 'EUR', 'CAD', 'CHF', 'AUD', 'SGD', 'KRW', 'JPY', 'PLN', 'GBP', 'SEK', 'NZD', 'RUB']


@bot.message_handler(state=MyStates.registration_name)
def get_name(message: Message) -> None:
    try:
        user = User.get(User.person_id == message.from_user.id)
    except User.DoesNotExist:
        bot.new_user = User(person_id=message.from_user.id, name=message.text)
    else:
        bot.new_user = User(id=user.id, person_id=user.person_id, name=message.text)
    store_message(message)

    bot.set_state(message.from_user.id, MyStates.registration_region, message.chat.id)
    bot.send_message(message.chat.id,
                     "Введите свой регион.\n(US, RU, ES, FR, UK, BR, IL, NL, CA, IT, CL, UA, PL, AU, DE, BE)")


@bot.message_handler(state=MyStates.registration_region)
def get_region(message: Message) -> None:
    store_message(message)
    if message.text in regions:
        bot.new_user.region = message.text
        bot.set_state(message.from_user.id, MyStates.registration_currency, message.chat.id)
        bot.send_message(message.chat.id,
                         "Введите валюту для отображения\n"
                         "USD, EUR, CAD, CHF, AUD, SGD, KRW, JPY, PLN, GBP, SEK, NZD, RUB")
    else:
        bot.send_message(message.chat.id, "Проверьте свой ввод.")


@bot.message_handler(state=MyStates.registration_currency)
def get_currency(message: Message) -> None:
    store_message(message)
    if message.text in currencies:
        bot.new_user.currency = message.text
        bot.delete_state(message.from_user.id, message.chat.id)
        bot.new_user.save()
        bot.send_message(message.chat.id, "Данные сохранены")
    else:
        bot.send_message(message.chat.id, "Проверьте свой ввод")

