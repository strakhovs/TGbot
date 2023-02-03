import datetime
from settings import BotSettings
import telebot

site = BotSettings()
token = site.bot_token.get_secret_value()
bot = telebot.TeleBot(token)


def log(message: telebot.types.Message):
    with open('log.txt', 'a+') as log_file:
        log_string = str(datetime.datetime.now()) + ' ' + str(message.from_user.first_name) + ' ' + str(message.text) + '\n'
        log_file.write(log_string)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')
    log(message)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Это бот!\nДоступные команды:\n/start\n/help\n/hello_world')
    log(message)


@bot.message_handler(commands=['hello_world'])
def hello_world(message):
    bot.send_message(message.chat.id, "Привет, мир! ✌️")
    log(message)


@bot.message_handler(content_types=['text'])
def reply_message(message):
    text = message.text.lower()
    if text == 'привет':
        bot.send_message(message.chat.id, 'Привет, я бот, пока без цели, но в ожидании...')
    else:
        bot.send_message(message.chat.id, 'Ничего не могу ответить на это. Наберите /help для помощи.')
    print(message.chat.id)
    print(message.text)
    log(message)


if __name__ == '__main__':
    bot.infinity_polling()
