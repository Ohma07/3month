# config.py
from aiogram import Bot, Dispatcher
from decouple import config


token = config("TOKEN")

bot = Bot(token=token)
dp = Dispatcher(bot)

Admins = [981877554, ]