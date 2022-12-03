from feedbackb.keyboards.text_templates import intro_text, talk_about_message
from aiogram.types.message import ContentType
from feedbackb.keyboards.inline import get_yes_no_keys
from feedbackb.utils.feedback_formater import message_format
from aiogram.dispatcher import FSMContext
from feedbackb.states.user_states import UserState
from feedbackb.handlers.start import send_welcome
from feedbackb.loader import dp, bot
from aiogram import types
from time import sleep


@dp.message_handler(content_types=ContentType.TEXT, state=UserState.started)
async def meeting_message(message: types.Message, state: FSMContext):
    print(message.message_id)
    if message.text.startswith('/'):
        await send_welcome(message, state)
        return

    first_name = message.text.strip()

    await bot.send_message(message.from_user.id,
                           f"Рад знакомству, {first_name}!☺️")

    await state.update_data(first_name=first_name)
    if message.from_user.username is not None:
        await state.update_data(username=message.from_user.username)
    else:
        await state.update_data(username=None)

    await UserState.geted_feedback.set()

    sleep(1)

    await bot.send_message(message.from_user.id, intro_text)
    await bot.send_message(message.from_user.id, talk_about_message)


@dp.message_handler(state=UserState.geted_feedback)
async def confirm_message(message: types.Message, state: FSMContext):
    print(message.message_id)
    if message.text.startswith('/'):
        await send_welcome(message, state)
        return

    await state.update_data(user_feedback_text=message.text)
    await state.update_data(msg_id=message.message_id)
    data = await state.get_data()

    if data['username'] is not None:
        formated_message = await message_format(data, True)
    else:
        formated_message = await message_format(data, False)

    await state.update_data(finish_feedback_text=formated_message)
    await UserState.confirm.set()

    await bot.send_message(message.from_user.id, formated_message)
    await bot.send_message(message.from_user.id,
                           'Проверьте, пожалуйста, отзыв. Всё ли правильно?',
                           reply_markup=get_yes_no_keys())
