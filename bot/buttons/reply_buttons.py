import json

import requests
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot.buttons.text import back_main_menu, adverts, none_advert, forward_advert, back_admin_menu, back_main_menu_ru, \
    choice_language, choice_language_ru, get_guarantees, get_guarantees_ru, call_center, call_center_ru, help, help_ru


async def main_menu_buttons(chat_id: int):
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8001/telegram-users/chat_id/{chat_id}/").content)
    if tg_user['language'] == 'uz':
        design = [
            [get_guarantees],
            [call_center, help],
            [choice_language]
        ]
    else:
        design = [
            [get_guarantees_ru],
            [call_center_ru, help_ru],
            [choice_language_ru]
        ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def back_main_menu_button(chat_id: int):
    tg_user = json.loads(requests.get(url=f"http://127.0.0.1:8001/telegram-users/chat_id/{chat_id}/").content)
    if tg_user['language'] == 'uz':
        design = [[back_main_menu]]
    else:
        design = [[back_main_menu_ru]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def back_admin_menu_button():
    design = [[back_admin_menu]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def admin_menu_buttons():
    design = [
        [adverts],
        [back_main_menu]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def advert_menu_buttons():
    design = [
        [none_advert, forward_advert],
        [back_admin_menu]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


with open('data.json', 'r', encoding='utf-8') as f:
    region_data = json.load(f)


async def get_region_buttons():
    regions = [item["region"] for item in region_data]
    buttons = [KeyboardButton(text=region) for region in regions]
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    return keyboard


async def get_district_buttons(region_name):
    districts = next((item['districts'] for item in region_data if item["region"] == region_name), [])
    buttons = [KeyboardButton(text=district) for district in districts]
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    return keyboard


async def get_shops_button(lang):
    shops = json.loads(requests.get(url="http://127.0.0.1:8001/shops/").content)['results']
    design = []
    for shop in shops:
        design.append([f"{shop['id']}. {shop['name']}"])
    if lang == 'ru':
        design.append([back_main_menu_ru])
    else:
        design.append([back_main_menu])
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def get_types_button(lang):
    shops = json.loads(requests.get(url="http://127.0.0.1:8001/types/").content)['results']
    design = []
    row = []
    for shop in shops:
        row.append(KeyboardButton(f"{shop['id']}. {shop['name']}"))
        if len(row) == 2:
            design.append(row)
            row = []
    if row:
        design.append(row)
    if lang == 'ru':
        design.append([KeyboardButton(back_main_menu_ru)])
    else:
        design.append([KeyboardButton(back_main_menu)])
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
