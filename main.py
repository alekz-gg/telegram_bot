import telebot

token = "5264948128:AAEDHAcbIvCXcOENgFTJZaLEOin53wyZWQw"

bot = telebot.TeleBot(token)

start = """
/start - показать справку
/shoksha - выбрать шокшу
/poksha - выбрать покшу
/who_is_shoksha - узнать кто шокша
/who_is_poksha - узнать кто покша"""

# /poksha
# /who_is_poksha - узнать кто покша в этом чате сегодня
# /rating - кто есть кто

Shoksha = ''
Poksha = ''

def get_rate(message, task):
    pass

@bot.message_handler(commands=["start"])
def help(message):
    bot.send_message(message.chat.id, start)

# про шокшу
@bot.message_handler(commands=["shoksha"])
def shoksha(message):
    global Shoksha
    Shoksha = message.from_user.username
    text = ' теперь ты, @' + Shoksha + ', шокша'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["who_is_shoksha"])
def who_is_shoksha(message):
    if Shoksha:
        text = '@' + Shoksha + ' шокша'
        bot.send_message(message.chat.id, text)
    else:
        text = "Шокша еще не определён"
        bot.send_message(message.chat.id, text)

# про покшу
@bot.message_handler(commands=["poksha"])
def poksha(message):
    global Poksha
    Poksha = message.from_user.username
    text = ' теперь @' + Poksha + ' покша'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["who_is_poksha"])
def who_is_poksha(message):
    if Poksha:
        text = '@' + Poksha + ' покша'
        bot.send_message(message.chat.id, text)
    else:
        text = "Покша еще не определён"
        bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["show"])
def show(message):
    pass

# Постоянно обращается к серверу телеграмма
bot.polling(none_stop=True)

def choose(commands=[]):
    pass

# test_git_commit