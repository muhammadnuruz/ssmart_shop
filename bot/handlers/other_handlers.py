from aiogram import types
from aiogram.dispatcher.filters import Text

from bot.buttons.text import help, help_ru, call_center_ru, call_center
from bot.dispatcher import dp


@dp.message_handler(Text(equals=[call_center_ru, call_center]))
async def get_guarantees_function(msg: types.Message):
    await msg.answer(text=f"{msg.text} : +998508080055")


@dp.message_handler(Text(equals=[help, help_ru]))
async def get_guarantees_function(msg: types.Message):
    await msg.answer(text=f"{msg.text} : +998508080055")
