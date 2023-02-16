from telebot.types import Message
from loguru import logger
from database.CRUD import get_history, get_user
from handlers.custom_handlers.unknown_user import user_registration
from keyboards.inline.url_button import url_button
from loader import bot


@bot.message_handler(commands=["history"])
def history_command(message: Message) -> None:
    """
    Обработка команды /history
    """
    logger.debug(f'Вызвана команда /history, пользователь: {message.from_user.id}')
    bot.current_user = get_user(message.from_user.id)
    if bot.current_user:
        responses = get_history(int(message.from_user.id))
        if responses:
            for item in responses:
                response_list = eval(item['response'])
                for response in response_list:
                    resp_split = response.split('http')
                    bot.send_message(message.chat.id, resp_split[0],
                                     reply_markup=url_button('http'+''.join(resp_split[1])))
        else:
            bot.send_message(message.chat.id, 'История пуста')
    else:
        user_registration(message)
