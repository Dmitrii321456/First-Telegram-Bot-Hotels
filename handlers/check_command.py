from datetime import datetime
from loguru import logger
import telebot
from telebot import types
from logs.logers import func_loggers
from config import API_KEY, BOT_TOKEN

DEFAULT_COMMANDS = {
    "/start":  "Запуск бота, создает профиль",
    "/help": "Возможности бота и подробна информация",
    "/low": "Выводит самые дешевые отели",
    "/high": "Выводит самые дорогие отели",
    "/custom":  "Вывод поиска отеля по расстоянию",
    "/history": "Выводит историю поиска ",
}


@func_loggers
def get_commands(commands_dict):
    """Выводит список команд"""
    try:
        keyboards = types.InlineKeyboardMarkup(row_width=2)
        buttons = []
        for k, v in commands_dict.items():
            button = types.InlineKeyboardButton(v, callback_data=k)
            buttons.append(button)
        keyboards.add(*buttons)
        return keyboards
    except Exception as e:
        logger.error(f'Function error {e}')