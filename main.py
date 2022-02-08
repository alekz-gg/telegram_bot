from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import time


TOKEN="5264948128:AAEDHAcbIvCXcOENgFTJZaLEOin53wyZWQw"

bot = Bot(TOKEN)
dp = Dispatcher(bot)

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
    await message.reply("Обязательно бахнем")
    time.sleep(2)
    await bot.send_message(message.from_user.id, "И не раз")
    time.sleep(2)
    await bot.send_message(message.from_user.id, "Весь мир в труху")
    # await bot.send_message(message.from_user.id, "но через ", time_to_next_party())

"""========================ADMIN========================"""

async def next_party():
    pass

async def time_to_next_party():
    pass

async def get_friday(ctime):
    pass

"""========================GENERAL========================"""

HELP = """
/start - показать справку
/mojet_bahnem
"""

@dp.message_handler()
async def help(message: types.Message):
    if message.text.lower() == "Привет".lower():
        # await message.answer("Ну здарова")
        # await message.reply(message.text)
        await bot.send_message(message.from_user.id, HELP)

executor.start_polling(dp, skip_updates=True)







# start = """
# /start - показать справку
# /shoksha - выбрать шокшу
# /poksha - выбрать покшу
# /who_is_shoksha - узнать кто шокша
# /who_is_poksha - узнать кто покша"""

# # /poksha
# # /who_is_poksha - узнать кто покша в этом чате сегодня
# # /rating - кто есть кто

# Shoksha = ''
# Poksha = ''

# def get_rate(message, task):
#     pass

# @bot.message_handler(commands=["start"])
# def help(message):
#     bot.send_message(message.chat.id, start)

# # про шокшу
# @bot.message_handler(commands=["shoksha"])
# def shoksha(message):
#     global Shoksha
#     Shoksha = message.from_user.username
#     text = ' теперь ты, @' + Shoksha + ', шокша'
#     bot.send_message(message.chat.id, text)

# @bot.message_handler(commands=["who_is_shoksha"])
# def who_is_shoksha(message):
#     if Shoksha:
#         text = '@' + Shoksha + ' шокша'
#         bot.send_message(message.chat.id, text)
#     else:
#         text = "Шокша еще не определён"
#         bot.send_message(message.chat.id, text)

# # про покшу
# @bot.message_handler(commands=["poksha"])
# def poksha(message):
#     global Poksha
#     Poksha = message.from_user.username
#     text = ' теперь @' + Poksha + ' покша'
#     bot.send_message(message.chat.id, text)

# @bot.message_handler(commands=["who_is_poksha"])
# def who_is_poksha(message):
#     if Poksha:
#         text = '@' + Poksha + ' покша'
#         bot.send_message(message.chat.id, text)
#     else:
#         text = "Покша еще не определён"
#         bot.send_message(start = """
# /start - показать справку
# /shoksha - выбрать шокшу
# /poksha - выбрать покшу
# /who_is_shoksha - узнать кто шокша
# /who_is_poksha - узнать кто покша"""

# # /poksha
# # /who_is_poksha - узнать кто покша в этом чате сегодня
# # /rating - кто есть кто

# Shoksha = ''
# Poksha = ''

# def get_rate(message, task):
#     pass

# @bot.message_handler(commands=["start"])
# def help(message):
#     bot.send_message(message.chat.id, start)

# # про шокшу
# @bot.message_handler(commands=["shoksha"])
# def shoksha(message):
#     global Shoksha
#     Shoksha = message.from_user.username
#     text = ' теперь ты, @' + Shoksha + ', шокша'
#     bot.send_message(message.chat.id, text)

# @bot.message_handler(commands=["who_is_shoksha"])
# def who_is_shoksha(message):
#     if Shoksha:
#         text = '@' + Shoksha + ' шокша'
#         bot.send_message(message.chat.id, text)
#     else:
#         text = "Шокша еще не определён"
#         bot.send_message(message.chat.id, text)

# # про покшу
# @bot.message_handler(commands=["poksha"])
# def poksha(message):
#     global Poksha
#     Poksha = message.from_user.username
#     text = ' теперь @' + Poksha + ' покша'
#     bot.send_message(message.chat.id, text)

# @bot.message_handler(commands=["who_is_poksha"])
# def who_is_poksha(message):
#     if Poksha:
#         text = '@' + Poksha + ' покша'
#         bot.send_message(message.chat.id, text)
#     else:
#         text = "Покша еще не определён"
#         bot.send_message(message.chat.id, text)


# @bot.message_handler(commands=["show"])
# def show(message):
#     pass

# # Постоянно обращается к серверу телеграмма
# bot.polling(none_stop=True)

# def choose(commands=[]):
#     pass

# # test_git_commit