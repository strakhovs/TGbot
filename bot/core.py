import telebot


token = '5933331317:AAEqwCXmNKmgHuCKF18D8CxEfX7wzMkT420'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Это бот!\nДоступные команды:\n/start\n/help\n/hello_world')


@bot.message_handler(commands=['hello_world'])
def hello_world(message):
    bot.send_message(message.chat.id, "Привет, мир! ✌️")


@bot.message_handler(content_types=['text'])
def reply_message(message):
    text = message.text.lower()
    if text == 'привет':
        bot.send_message(message.chat.id, 'Привет, я бот, пока без цели, но в ожидании...')
    else:
        bot.send_message(message.chat.id, 'Ничего не могу ответить на это. Наберите /help для помощи.')
    print(message.chat.id)
    print(message.text)


if __name__ == '__main__':
    bot.infinity_polling()
