from aiogram import Dispatcher, types
from datetime import datetime, timedelta
from create_bot import dp, bot
import time

@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Здравствуй, мой юный друг", )
        await message.delete()
    except:
        await message.reply("Общение с ботом через ЛС, напишите ему :\nhttps://t.me/wtf_repeat_bot")

@dp.message_handler(commands=['mojet_bahnem'])
async def command_mojet_bahnem(message: types.Message):
    friday = message.date + timedelta( (4-message.date.weekday()) % 7 )
    party = datetime(friday.year, friday.month, friday.day, hour=19, minute=00, second=00)
    time_to_party = party - message.date
    await message.reply("Обязательно бахнем")
    time.sleep(1)
    await bot.send_message(message.from_user.id, "И не раз")
    time.sleep(1)
    await bot.send_message(message.from_user.id, "Весь мир в труху")
    time.sleep(1)
    await bot.send_message(message.from_user.id, f'но через {time_to_party}')

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_mojet_bahnem, commands=['mojet_bahnem'])
    # dp.register_message_handler()