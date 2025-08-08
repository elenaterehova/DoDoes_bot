from aiogram import types
from config import dp


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Приветик")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

