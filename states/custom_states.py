from telebot.handler_backends import State, StatesGroup


class MyStates(StatesGroup):
    search_low = State()
    search_high = State()
    search_custom_start = State()
    search_custom_end = State()
    search_custom = State()
    search_layout = State()
    search_range = State()
