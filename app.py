from utils.set_bot_commands import set_default_commands
from aiogram import executor
from loader import dp
import handlers
import logging


async def on_startup(dispatcher):
    logging.basicConfig(level=logging.INFO)
    await set_default_commands(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
