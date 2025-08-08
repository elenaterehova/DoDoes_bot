from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Кнопка'))
    return kb
