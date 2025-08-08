from aiogram import types
from config import dp
from keyboards import get_main_kb


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Приветик", reply_markup=get_main_kb())


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
