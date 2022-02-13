from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot

class FSMAdmin(StatesGroup):
    name = State()
    descrition = State()
    date = State()
    time = State()

# Начало диалога создания нового события
@dp.message_handler(commands="Add_event", State=None)
async def add_event(message: types.Message):
    await FSMAdmin.name.set()
    await message.reply('Напиши название мероприятия')

# Ловим первый ответ и пишем в словарь
@dp.message_handler(state=FSMAdmin.name)
async def add_event_name(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply("Введи описание")

# Ловим второй ответ с описанием пероприятия
@dp.message_handler(state=FSMAdmin.descrition)
async def add_event_descrition(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['descrition'] = message.text
    await FSMAdmin.next()
    await message.reply("Когда? Введи дату в формате ДД-ММ-ГГГГ")

# Ловим третий ответ с датой
@dp.message_handler(state=FSMAdmin.date)
async def add_event_date(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
    await FSMAdmin.next()
    await message.reply("Когда? Введи время в формате ЧЧ-ММ")

# Ловим четвертый ответ с временем
@dp.message_handler(state=FSMAdmin.time)
async def add_event_time(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['time'] = message.text
    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(add_event, commands=['Add_event'], state=None)
    dp.register_message_handler(add_event_name, state=FSMAdmin.name)
    dp.register_message_handler(add_event_descrition, state=FSMAdmin.descrition)
    dp.register_message_handler(add_event_date, state=FSMAdmin.date)
    dp.register_message_handler(add_event_time, state=FSMAdmin.time)