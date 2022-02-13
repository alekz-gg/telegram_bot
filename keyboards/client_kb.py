from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/mojet_bahnem')
b2 = KeyboardButton('/start')
b3 = KeyboardButton('Позвоните мне', request_contact=True)
b4 = KeyboardButton('Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)


kb_client.add(b1).add(b2).add(b3).insert(b4)
