from telebot.types import Message, ReplyKeyboardRemove
from loguru import logger
from database.CRUD import store_message
from database.models import User
from keyboards.reply.region_keyboard import region_keyboard, currency_keyboard
from loader import bot
from states.custom_states import MyStates


regions = ['US', 'RU', 'ES', 'FR', 'UK', 'BR', 'IL', 'NL', 'CA', 'IT', 'CL', 'UA', 'PL', 'AU', 'DE', 'BE']
currencies = ['USD', 'EUR', 'CAD', 'CHF', 'AUD', 'SGD', 'KRW', 'JPY', 'PLN', 'GBP', 'SEK', 'NZD', 'RUB']


@bot.message_handler(state=MyStates.registration_name)
def get_name(message: Message) -> None:
    """
    Сохранение имени, переход к запросу региона
    """
    try:
        user = User.get(User.person_id == message.from_user.id)
    except User.DoesNotExist:
        logger.exception('Пользователь не найден')
        bot.new_user = User(person_id=message.from_user.id, name=message.text)
    else:
        bot.new_user = User(id=user.id, person_id=user.person_id, name=message.text)
    store_message(message)

    bot.set_state(message.from_user.id, MyStates.registration_region, message.chat.id)
    bot.send_message(message.chat.id,
                     "Выберите свой регион.",
                     reply_markup=region_keyboard())


@bot.message_handler(state=MyStates.registration_region)
def get_region(message: Message) -> None:
    """
    Сохранение региона, переход к запросу валюты
    """
    store_message(message)
    if message.text in regions:
        bot.new_user.region = message.text
        bot.set_state(message.from_user.id, MyStates.registration_currency, message.chat.id)
        bot.send_message(message.chat.id,
                         "Выберите валюту для отображения",
                         reply_markup=currency_keyboard())
    else:
        bot.send_message(message.chat.id, "Проверьте свой ввод.")


@bot.message_handler(state=MyStates.registration_currency)
def get_currency(message: Message) -> None:
    """
    Сохранение пользователя в БД, сброс состояния
    """
    store_message(message)
    if message.text in currencies:
        bot.new_user.currency = message.text
        bot.delete_state(message.from_user.id, message.chat.id)
        bot.new_user.save()
        bot.send_message(message.chat.id, "Данные сохранены", reply_markup=ReplyKeyboardRemove())
    else:
        bot.send_message(message.chat.id, "Проверьте свой ввод")
