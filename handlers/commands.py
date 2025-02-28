# commands.py
from aiogram import types, Dispatcher, executor
from config import bot,dp
import random
import buttons



async def start_hanler(message: types.Message):
    print('Обработчик старта')
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello {message.from_user.first_name}\n'
                                f'Твой Telegram ID - {message.from_user.id}\n', reply_markup=buttons.start)

    await message.answer('Привет мир')


async def mem_handler(message: types.Message):
    # photo = open('media/images.jpeg', 'rb')

    with open('media/meme.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo)


# @dp.message_handler()
# async def echo(message: types.Message):
#     text = message.text.lower()
#
#     if "game" in text:
#         games_list = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']
#         chosen_game = random.choice(games_list)
#         await message.answer(f"Игральная кость выбрана: {chosen_game}")
#         await bot.send_dice(message.chat.id, emoji=chosen_game)
#     else:
#         await message.reply(f"Вы написали: {message.text}")
#

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_hanler, commands=['start'])
    dp.register_message_handler(mem_handler, commands=['mem'])


