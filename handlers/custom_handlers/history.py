from telebot.types import Message

from database.CRUD import store_message, get_history
from loader import bot


@bot.message_handler(commands=["history"])
def history_command(message: Message) -> None:
    """
    Обработка команды /history
    """

    responses = get_history(int(message.from_user.id))
    for item in responses:

        response_list = eval(item['response'])
        for response in response_list:
            bot.send_message(message.chat.id, response)
