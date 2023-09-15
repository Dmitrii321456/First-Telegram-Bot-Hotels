from pprint import pprint
from sqlite3 import IntegrityError
from typing import Dict

import telebot
import telebot.util
import telebot.types
from telebot.util import quick_markup
from telebot import types
from loguru import logger

from config import BOT_TOKEN, API_KEY
from utils.founding_city import find_cities
from handlers.check_command import DEFAULT_COMMANDS
from datebase.forms import User

bot = telebot.TeleBot(BOT_TOKEN)
api_key = API_KEY

CITY = ''
CITIES = {}


@bot.message_handler(commands=['start'])
def start_telebot(message):
    bot.reply_to(message, f'Добро пожаловать, {message.from_user.first_name}!')


