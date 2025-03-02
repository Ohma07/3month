from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from db import main_db
import buttons
from config import Admins


class StoreFSM(StatesGroup):
    name_product = State()
    size = State()
    price = State()
    category = State()
    info_product = State()
    products_id = State()
    photo = State()
    submit = State()


async def start_fsm_store(message: types.Message):
    if message.from_user.id not in Admins:
        await message.answer('У вас нет доступа к этой команде.')
        return

    await message.answer('Введите название товара:', reply_markup=buttons.cancel_fsm)
    await StoreFSM.name_product.set()


async def name_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_product'] = message.text

    await StoreFSM.next()
    await message.answer('Введите размер:')


async def size_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size_product'] = message.text

    await StoreFSM.next()
    await message.answer('Введите цену товара:')

async def price_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price_product'] = message.text

    await StoreFSM.next()
    await message.answer('Введите категорию товара:')


async def category_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category_product'] = message.text

    await StoreFSM.next()
    await message.answer('Введите информацию о продукте:')


async def info_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info_product'] = message.text

    await StoreFSM.next()
    await message.answer('Введите артикул для товара: ')


async def product_id_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['products_id'] = message.text

    await StoreFSM.next()
    await message.answer("Отправьте фото товара:")

async def photo_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await StoreFSM.next()
    await message.answer('Верные ли данные ?', reply_markup=buttons.submit)
    await message.answer_photo(photo=data['photo'],
                               caption=f'Название товара - {data["name_product"]}\n'
                                       f'Размер товара - {data["size_product"]}\n'
                                       f'Категория - {data["category_product"]}\n'
                                       f'Артикул - {data["products_id"]}\n'
                                       f'Инфо - {data["info_product"]}\n'
                                       f'Цена - {data["price_product"]}')


async def submit_load(message: types.Message, state: FSMContext):
    if message.text == 'да':
        async with state.proxy() as data:
            await main_db.sql_insert_store(
                name_product=data['name_product'],
                size=data['size_product'],
                price=data['price_product'],
                product_id=data['products_id'],
                photo=data['photo']
            )

            await main_db.sql_insert_store_detail(
                product_id=data['products_id'],
                info_product=data['info_product'],
                category=data['category_product']
            )

            await message.answer('Ваши данные в базе!', reply_markup=buttons.remove_keyboard)
            await state.finish()
    elif message.text == 'нет':
        await message.answer('Хорошо, отменено!', reply_markup=buttons.remove_keyboard)
        await state.finish()

    else:
        await message.answer('Выберите да или нет')


def register_handlers_store(dp: Dispatcher):
    dp.register_message_handler(start_fsm_store, commands=['registration'])
    dp.register_message_handler(name_load, state=StoreFSM.name_product)
    dp.register_message_handler(size_load, state=StoreFSM.size)
    dp.register_message_handler(price_load, state=StoreFSM.price)
    dp.register_message_handler(category_load, state=StoreFSM.category)
    dp.register_message_handler(info_load, state=StoreFSM.info_product)
    dp.register_message_handler(product_id_load, state=StoreFSM.products_id)
    dp.register_message_handler(photo_load, state=StoreFSM.photo, content_types=['photo'])
    dp.register_message_handler(submit_load, state=StoreFSM.submit)


# class FSMProduct(StatesGroup):
#     name = State()
#     size = State()
#     category = State()
#     price = State()
#     photo = State()
#     submit = State()
#
# async def start_fsm_product(message: types.Message):
#     await FSMProduct.name.set()
#     await message.answer('Введите название модели товара: ')
#
# async def load_name(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['name'] = message.text
#     await FSMProduct.next()
#     await message.answer('Введите размер товара: ')
#
# async def load_size(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['size'] = message.text
#     await FSMProduct.next()
#     await message.answer('Введите категорию товара: ')
#
# async def load_category(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['category'] = message.text
#     await FSMProduct.next()
#     await message.answer('Введите стоимость товара: ')
#
# async def load_price(message: types.Message, state: FSMContext):
#     if not message.text.isdigit():
#         await message.answer('Пожалуйста, введите числовое значение для цены.')
#         return
#     async with state.proxy() as data:
#         data['price'] = int(message.text)
#     await FSMProduct.next()
#     await message.answer('Загрузите фото товара: ')
#
# async def load_photo(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['photo'] = message.photo[-1].file_id
#     await FSMProduct.next()
#     await message.answer('Подтвердите добавление товара')
#     await message.answer_photo(photo=data['photo'],
#                                caption=f'Название: {data["name"]}\n'
#                                        f'Размер: {data["size"]}\n'
#                                        f'Категория: {data["category"]}\n'
#                                        f'Стоимость: {data["price"]} руб.\n')
#
# async def submit_product(message: types.Message, state: FSMContext):
#     if message.text.lower() == 'да':
#         async with state.proxy() as data:
#             # Запись в базу
#             await message.answer('Товар добавлен в базу.')
#         await state.finish()
#     elif message.text.lower() == 'нет':
#         await message.answer('Добавление товара отменено.')
#         await state.finish()
#     else:
#         await message.answer('Выберите "да" или "нет".')
#
# def register_handlers_fsm(dp: Dispatcher):
#     dp.register_message_handler(start_fsm_product, commands=['add_product'])
#     dp.register_message_handler(load_name, state=FSMProduct.name)
#     dp.register_message_handler(load_size, state=FSMProduct.size)
#     dp.register_message_handler(load_category, state=FSMProduct.category)
#     dp.register_message_handler(load_price, state=FSMProduct.price)
#     dp.register_message_handler(load_photo, state=FSMProduct.photo, content_types=['photo'])
#     dp.register_message_handler(submit_product, state=FSMProduct.submit)
