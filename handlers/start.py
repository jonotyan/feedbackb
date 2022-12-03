from aiogram.types.message import ContentType
from aiogram.dispatcher import FSMContext
from feedbackb.states.user_states import UserState
from feedbackb.loader import dp, bot
from aiogram import types
from time import sleep


# ----------------------------------------------- START USER MESSAGE
@dp.message_handler(commands=['start'], content_types=ContentType.TEXT)
async def send_welcome(message: types.Message, state: FSMContext):
    print(message.message_id)
    await state.reset_state()
    await bot.send_message(message.from_user.id,
                           "Приветствую!💫")
    sleep(1)
    await UserState.started.set()
    await bot.send_message(message.from_user.id,
                           "Меня зовут бот Альфи. А как Вас зовут?")
