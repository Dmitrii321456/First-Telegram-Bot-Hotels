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
from utils.founding_city import find_cities, get_key_by_value
from handlers.check_command import DEFAULT_COMMANDS
from datebase.forms import User
from handlers.start import start_telebot
from handlers.check_command import get_commands

bot = telebot.TeleBot(BOT_TOKEN)
api_key = API_KEY


def type_money(message):
    valut = message
    bot.reply_to(message, valut)

