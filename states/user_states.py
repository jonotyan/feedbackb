from aiogram.dispatcher.filters.state import State, StatesGroup


class UserState(StatesGroup):
    started = State()
    geted_name = State()
    geted_feedback = State()
    confirm = State()
    finish = State()
