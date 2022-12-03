from aiogram import types
from feedbackb.loader import dp, bot
from feedbackb.data.config import CHANNEL_ID
from feedbackb.states.user_states import UserState
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(state=UserState.confirm)
async def show_menu(call: types.CallbackQuery, state: FSMContext):
    # ----------------------------------------------- CALLBACKS PUBLISH & REMAKE FEEDBACK
    if call.data == 'publish':
        feedback = await state.get_data()
        if feedback['username'] is not None:
            await bot.send_message(CHANNEL_ID, feedback['finish_feedback_text'])
            # await call.message.edit_text()
        else:
            await bot.send_message(CHANNEL_ID, feedback['finish_feedback_text'])
        await state.finish()
        await call.message.edit_text('Благодарю Вас! Опубликовал отзыв в @openlakefeedback. Желаю отличного дня☀️')

    elif call.data == 'remake':
        await UserState.geted_feedback.set()
        await call.message.edit_text('Ожидаю нового отзыва')
