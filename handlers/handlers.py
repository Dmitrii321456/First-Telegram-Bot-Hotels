from sqlite3 import IntegrityError
from config import BOT_TOKEN, API_KEY
import telebot

from datebase.forms import User

bot = telebot.TeleBot(BOT_TOKEN)
api_key = API_KEY

DEFAULT_COMMANDS = (
    ("start", "Запуск бота, создает профиль"),
    ("help", "Показывает возможности бота"),
    ("low", "Выводит минимальные показатели поиска"),
    ("high", "Выводит максимальные показатели поиска"),
    ("custom", "Вывод показателей пользовательского диапазона"),
    ("history", "Выводит историю поиска "),
)


@bot.message_handler(commands=['start'])
def handler_start(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    try:
        User.create(
            user_id=user_id,
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
        )
        bot.reply_to(message, "Добро пожаловать.")
    except IntegrityError:
        bot.reply_to(message, 'Рад вас снова видеть {first_name}'.format(first_name=first_name))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


def run_bot():
    bot.infinity_polling()
