from cgitb import text
from posixpath import split
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

import time, json, string


TOKEN="5264948128:AAEDHAcbIvCXcOENgFTJZaLEOin53wyZWQw"

bot = Bot(TOKEN)
dp = Dispatcher(bot)

fucking_dict = {}

"""========================CLIENT========================"""

@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Здравствуй, мой юный друг", )
        await message.delete()
    except:
        await message.reply("Общение с ботом через ЛС, напишите ему :\nhttps://t.me/wtf_repeat_bot")

@dp.message_handler(commands=['mojet_bahnem'])
async def command_start(message: types.Message):
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

"""========================ADMIN========================"""

async def next_party():
    pass

# @dp.message_handler()
# async def time_to_next_party(message):
#     friday = message.date + timedelta( (4-today.weekday()) % 7 )
#     party = datetime(friday.year, friday.month, friday.day, hour=19, minute=00, second=00)
#     time_to_party = party - message.date
#     return time_to_party

# def get_friday(ctime):
#     friday = today + timedelta( (4-today.weekday()) % 7 )
#     pass

"""========================GENERAL========================"""



HELP = """
/start - показать справку
/mojet_bahnem
"""

@dp.message_handler()
async def fucking_checking(message: types.Message):
    for word in message.text.split():
        if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split()}\
            .intersection(set(json.load(open('cenz.json')))) != set():
            await message.reply('Ах ты матершинник')
            if message.from_user.id in list(fucking_dict.keys()):
                fucking_dict[message.from_user.username] = str(int(fucking_dict[message.from_user.username]) + 1)
            else:
                fucking_dict[message.from_user.username] = 1
            text = 'Главный матершинник чата ' + str(fucking_rating())
            await bot.send_message(message.chat.id, text)

def fucking_rating():
    top = sorted(list(fucking_dict.values()))[0]
    def get_key(fucking_dict, top):
        for user_id, value in fucking_dict.items():
            if value == top:
                return user_id    
    fucking_top = get_key(fucking_dict, top)
    return fucking_top

executor.start_polling(dp, skip_updates=True)