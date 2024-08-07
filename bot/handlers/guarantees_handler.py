import json
from datetime import datetime

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.buttons.reply_buttons import get_shops_button, get_types_button, back_main_menu_button, main_menu_buttons
from bot.buttons.text import get_guarantees, get_guarantees_ru
from bot.dispatcher import dp


@dp.message_handler(Text(equals=[get_guarantees, get_guarantees_ru]))
async def get_guarantees_function(msg: types.Message, state: FSMContext):
    await state.set_state('guarantees_1')
    if msg.text == get_guarantees:
        await msg.answer(text="Harid qilingan do'konni tanlang 👇", reply_markup=await get_shops_button(lang='uz'))
    else:
        await msg.answer(text="Выберите магазин, в котором был куплен 👇",
                         reply_markup=await get_shops_button(lang='ru'))


@dp.message_handler(state='guarantees_1')
async def get_guarantees_function_2(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['shop'] = msg.text.split('.')[0]
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8001/telegram-users/chat_id/{msg.from_user.id}/").content)
    await state.set_state('guarantees_2')
    if tg_user['language'] == 'uz':
        await msg.answer(text="Mahsulot turini tanlang 👇", reply_markup=await get_types_button(lang='uz'))
    else:
        await msg.answer(text="Выберите тип продукта 👇",
                         reply_markup=await get_types_button(lang='ru'))


@dp.message_handler(state='guarantees_2')
async def get_guarantees_function_3(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = msg.text.split('.')[0]
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8001/telegram-users/chat_id/{msg.from_user.id}/").content)
    await state.set_state('guarantees_3')
    if tg_user['language'] == 'uz':
        await msg.answer(text="Seria raqamini kiriting:", reply_markup=await back_main_menu_button(msg.from_user.id))
    else:
        await msg.answer(text="Введите серийный номер:",
                         reply_markup=await back_main_menu_button(msg.from_user.id))


@dp.message_handler(state='guarantees_3')
async def get_guarantees_function_4(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['serial_number'] = msg.text
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8001/telegram-users/chat_id/{msg.from_user.id}/").content)
    await state.set_state('guarantees_4')
    if tg_user['language'] == 'uz':
        await msg.answer(
            text="""
Harid qilingan to'g'ri formatda kiriting:

Format: <b>kun-oy-yil</b>
Misol: <b>15-07-2024</b>""",
            reply_markup=await back_main_menu_button(msg.from_user.id), parse_mode="HTML")
    elif tg_user['language'] == 'ru':
        await msg.answer(
            text="""
Введите дату покупки в правильном формате:

Формат: <b>день-месяц-год</b>
Пример: <b>15-07-2024</b>""",
            reply_markup=await back_main_menu_button(msg.from_user.id), parse_mode="HTML")


@dp.message_handler(state='guarantees_4')
async def process_date(msg: types.Message, state: FSMContext):
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8001/telegram-users/chat_id/{msg.from_user.id}/").content)
    try:
        date_obj = datetime.strptime(msg.text, '%d-%m-%Y')
        formatted_date = date_obj.strftime('%Y-%m-%d')
        tg_user = json.loads(
            requests.get(url=f"http://127.0.0.1:8001/telegram-users/chat_id/{msg.from_user.id}/").content)
        async with state.proxy() as data:
            pass
        data_2 = {
            "shop": int(data['shop']),
            "type": int(data['type']),
            "serial_number": data['serial_number'],
            "date_of_purchase": formatted_date,
            "user": tg_user['id']
        }
        await state.finish()
        response = json.loads(requests.post(url=f"http://127.0.0.1:8001/guarantes/create/", data=data_2).content)
        if tg_user['language'] == 'uz':
            await msg.answer(f"""
Sizning {response['id']} - raqamli arizangizga asosan Kafolat taloni ruyhatga olindi

Kafolat muddati {response['validity_period']} - gacha

Qo'shimcha savollar uchun CALL MARKAZ - ga murojat qiling 😊""", reply_markup=await main_menu_buttons(msg.from_user.id))
        elif tg_user['language'] == 'ru':
            await msg.answer(f"""
На основании вашего {response['id']} – цифрового приложения зарегистрирован гарантийный талон.

Гарантийный срок составляет до {response['validity_period']}.

По дополнительным вопросам обращайтесь в CALL ЦЕНТР 😊""", reply_markup=await main_menu_buttons(msg.from_user.id))

    except ValueError:
        if tg_user['language'] == 'uz':
            await msg.answer("Iltimos, sanani to'g'ri formatda kiriting. Misol: 15-07-2024")
        elif tg_user['language'] == 'ru':
            await msg.answer("Пожалуйста, введите дату в правильном формате. Пример: 15-07-2024")
