from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN="5264948128:AAEDHAcbIvCXcOENgFTJZaLEOin53wyZWQw"

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=storage)