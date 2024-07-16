import json

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from bot.buttons.inline_buttons import language_buttons
from bot.buttons.reply_buttons import main_menu_buttons, get_district_buttons, get_region_buttons
from bot.buttons.text import back_main_menu, choice_language, choice_language_ru, back_main_menu_ru
from bot.dispatcher import dp, bot
from main import admins


@dp.message_handler(Text(equals=[back_main_menu, back_main_menu_ru]))
async def back_main_menu_function_1(msg: types.Message):
    if msg.text == back_main_menu:
        await msg.answer(text=f"Asosiy menu🏠", reply_markup=await main_menu_buttons(msg.from_user.id))
    elif msg.text == back_main_menu_ru:
        await msg.answer(text="Главное меню🏠", reply_markup=await main_menu_buttons(msg.from_user.id))


@dp.message_handler(Text(equals=[back_main_menu, back_main_menu_ru]),
                    state=['guarantees_1', 'guarantees_2', 'guarantees_3', 'guarantees_4'])
async def back_main_menu_function_1(msg: types.Message, state: FSMContext):
    await state.finish()
    if msg.text == back_main_menu:
        await msg.answer(text=f"Asosiy menu🏠", reply_markup=await main_menu_buttons(msg.from_user.id))
    elif msg.text == back_main_menu_ru:
        await msg.answer(text="Главное меню🏠", reply_markup=await main_menu_buttons(msg.from_user.id))


@dp.message_handler(CommandStart())
async def start_handler(msg: types.Message, state: FSMContext):
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{msg.from_user.id}/").content)
    try:
        if tg_user['detail']:
            await state.set_state('language_1')
            await msg.answer(text="""
Tilni tanlang

-------------

Выберите язык""", reply_markup=await language_buttons())
            data = {
                "chat_id": str(msg.from_user.id),
                "username": msg.from_user.username,
                "full_name": msg.from_user.full_name,
                "language": 'uz'
            }
            requests.post(url=f"http://127.0.0.1:8000/telegram-users/create/", data=data)
    except KeyError:
        if tg_user.get('language') == 'uz':
            await msg.answer(text=f"Bot yangilandi ♻️", reply_markup=await main_menu_buttons(msg.from_user.id))
        else:
            await msg.answer(text="Бот обновлен ♻️", reply_markup=await main_menu_buttons(msg.from_user.id))


@dp.callback_query_handler(Text(startswith='language_'), state='language_1')
async def language_function(call: types.CallbackQuery, state: FSMContext):
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{call.from_user.id}/").content)
    data = {
        "chat_id": str(call.from_user.id),
        "username": call.from_user.username,
        "full_name": call.from_user.full_name,
        "language": call.data.split("_")[-1]
    }
    requests.put(url=f"http://127.0.0.1:8000/telegram-users/update/{tg_user['id']}/", data=data)
    await call.message.delete()
    await state.set_state('register_1')
    async with state.proxy() as data:
        data['language'] = call.data.split("_")[-1]
    if call.data.split("_")[-1] == 'uz':
        await call.message.answer(text=f"Ism-Familiyangizni kiriting ✍️:")
    else:
        await call.message.answer(text=f"Введите свое имя и фамилию ✍️:")


@dp.message_handler(state='register_1')
async def register_function(msg: types.Message, state: FSMContext):
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{msg.from_user.id}/").content)
    async with state.proxy() as data:
        data['full_name'] = msg.text
    await state.set_state("register_2")
    if tg_user.get('language') == 'uz':
        k = KeyboardButton(text="TELEFON RAQAM📲", request_contact=True)
        kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        kb_client.add(k)
        await msg.answer(text="«TELEFON RAQAM📲» - tugmasi orqali telefon raqamingizni yuboring 👇",
                         reply_markup=kb_client)
    else:
        k = KeyboardButton(text="НОМЕР ТЕЛЕФОНА📲", request_contact=True)
        kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        kb_client.add(k)
        await msg.answer(text="Отправьте свой номер телефона через кнопку «НОМЕР ТЕЛЕФОНА📲» 👇", reply_markup=kb_client)


@dp.message_handler(state='register_2', content_types='contact')
async def phone_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["phone_number"] = msg.contact.phone_number
    if data['language'] == 'uz':
        await msg.answer("Regionni tanlang:", reply_markup=await get_region_buttons())
    else:
        await msg.answer("Выбрать регион:", reply_markup=await get_region_buttons())
    await state.set_state("select_region")


@dp.message_handler(state='select_region')
async def region_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['region'] = msg.text
    if data['language'] == 'uz':
        await msg.answer("Tumanni tanlang:", reply_markup=await get_district_buttons(msg.text))
    else:
        await msg.answer(text="Выберите район:", reply_markup=await get_district_buttons(msg.text))
    await state.set_state("select_district")


@dp.message_handler(state='select_district')
async def district_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    if data['language'] == 'uz':
        await msg.answer(text="Xush kelibsiz 😊", reply_markup=await main_menu_buttons(msg.from_user.id))
    else:
        await msg.answer(text="Добро пожаловать 😊", reply_markup=await main_menu_buttons(msg.from_user.id))
    data_2 = {
        'region': data['region'],
        'district': msg.text,
        'phone_number': data['phone_number'],
        'full_name': data['full_name'],
        'language': data['language']
    }
    tg_user = json.loads(
        requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{msg.from_user.id}/").content)
    requests.patch(url=f"http://127.0.0.1:8000/telegram-users/update/{tg_user['id']}/", data=data_2)
    for admin in admins:
        await bot.send_message(chat_id=admin, text=f"""
Yangi user🆕
ID: <a href='tg://user?id={msg.from_user.id}'>{msg.from_user.id}</a>
Ism-Familiya: {data['full_name']},
Username: @{msg.from_user.username}
Telefon-raqam: {data['phone_number']}
Region: {data['region']}
Tuman: {msg.text}""", parse_mode='HTML')
    await state.finish()


@dp.message_handler(Text(equals=[choice_language, choice_language_ru]))
async def change_language_function_1(msg: types.Message, state: FSMContext):
    if msg.text == choice_language:
        await msg.answer(text="Tilni tanlang", reply_markup=await language_buttons())
    else:
        await msg.answer(text="Выберите язык", reply_markup=await language_buttons())


@dp.callback_query_handler(Text(startswith='language_'))
async def language_function_1(call: types.CallbackQuery):
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{call.from_user.id}/").content)
    data = {
        "chat_id": str(call.from_user.id),
        "username": call.from_user.username,
        "full_name": call.from_user.full_name,
        "language": call.data.split("_")[-1]
    }
    requests.put(url=f"http://127.0.0.1:8000/telegram-users/update/{tg_user['id']}/", data=data)
    await call.message.delete()
    if call.data.split("_")[-1] == 'uz':
        await call.message.answer(text="Til o'zgartirildi 🇺🇿", reply_markup=await main_menu_buttons(call.from_user.id))
    else:
        await call.message.answer(text="Язык изменен 🇷🇺", reply_markup=await main_menu_buttons(call.from_user.id))
