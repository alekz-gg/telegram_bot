from aiogram import Dispatcher, types
from create_bot import dp, bot
import json, string


fucking_dict = {}

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

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(fucking_checking)