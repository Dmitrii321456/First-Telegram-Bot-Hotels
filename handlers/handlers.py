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

CITY = ''
CITIES = {}


@bot.message_handler(['start'])
def start_telebot(message):
    bot.send_message(message.from_user.id, 'Добро пожаловать в телеграм бот, он поможет вам подобрать подходящий '
                                           'отель по вашему желанию, выберите в меню подходящий для вас пункт.')
    bot.send_message(message.from_user.id, 'В каком городе вы хотите найти отель ?')
    bot.register_next_step_handler(message, check_commands)


def check_commands(message):
    global CITIES
    CITIES = find_cities(message.text)
    keyboards = get_commands(CITIES)
    bot.send_message(message.from_user.id, text='Выберите город:', reply_markup=keyboards)
    bot.register_next_step_handler(message, get_city)


def get_city(message):
    city = message.text
    city_id = get_key_by_value(CITIES, city)
    keyboards = types.InlineKeyboardMarkup(row_width=2)
    ru_button = types.InlineKeyboardButton('RU', callback_data='ru')
    usd_button = types.InlineKeyboardButton('USD', callback_data='usd')
    keyboards.add(ru_button, usd_button)
    bot.send_message(message.chat.id, text='Выберите валюту', reply_markup=keyboards)
    bot.register_next_step_handler(message, type_money)

def type_money(message):
    valut = message
    bot.reply_to(message, valut)




def run_bot():
    bot.infinity_polling()