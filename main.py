# main.py

from aiogram import executor
import logging
from handlers import commands, echo, quiz
from config import dp, Admins, bot


async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Бот включен!')


async def on_shutdown(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Бот выключен!')


# ====================================================================
commands.register_handlers(dp)
quiz.register_handlers(dp)


# ==========================
echo.register_handlers(dp)
# ====================================================================


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)

