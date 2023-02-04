from telebot.handler_backends import State, StatesGroup


class MyStates(StatesGroup):
    search = State()
    search_range = State()
