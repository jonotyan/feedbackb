from aiogram import types


def get_yes_no_keys():
    buttons = [
        types.InlineKeyboardButton(text='Всё верно', callback_data='publish'),
        types.InlineKeyboardButton(text='Переписать', callback_data='remake'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    return keyboard.add(*buttons)
