# quiz.py
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot


async def quiz(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton('Далее к вопросу 2', callback_data='button_qyuz_2')

    keyboard.add(button)

    question = 'Какое время года?'
    answer = ['Лето', "Зима", 'Осень', "Весна"]

    with open('media/meme.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='🍂',
        open_period=60,
        reply_markup=keyboard
    )


async def qyuz_2(call: types.CallbackQuery):
    await call.answer()
    question = 'Dota2 or CS.GO?'
    answer = ['Dota2', 'CS.GO', 'Valve']

    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton('Далее к вопросу 3', callback_data='button_qyuz_3')
    keyboard.add(button)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        reply_markup=keyboard
    )


async def qyuz_3(call: types.CallbackQuery):
    await call.answer()
    question = 'Favorite car?'
    answer = ['Mercedes', 'BMW', 'Lexus']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2
    )


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz, commands=['quiz'])
    dp.register_callback_query_handler(qyuz_2, text='button_qyuz_2')
    dp.register_callback_query_handler(qyuz_3, text='button_qyuz_3')




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)