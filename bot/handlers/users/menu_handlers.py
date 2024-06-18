from typing import Union

from aiogram import types
from aiogram.types import CallbackQuery, Message

from keyboards.inline.menu_keyboards import (
    menu_cd,
    product_keyboard,
    subproduct_keyboard,
    items_keyboard,
    item_keyboard,
)
from loader import dp, db


# Bosh menyu matni uchun handler
@dp.message_handler(text="Bosh menyu")
async def show_menu(message: types.Message):
    # Foydalanuvchilarga barcha kategoriyalarni qaytaramiz
    await list_items(message)


async def list_items(message: Message, **kwargs):
    markup = await items_keyboard()

    await message.answer(text="Mahsulot tanlang", reply_markup=markup)


# Biror mahsulot uchun Xarid qilish tugmasini yuboruvchi funksiya
async def show_item(callback: CallbackQuery, category, subcategory, item_id):

    # Mahsulot haqida ma'lumotni bazadan olamiz
    item = await db.get_product(item_id)

    if item["image"]:
        text = f"<a href=\"{item['image']}\">{item['name']}</a>\n\n"
    else:
        text = f"{item['name']}\n\n"
    text += f"Narxi: {item['price']}$\n{item['name']}"

    await callback.message.edit_text(text=text)


# Yuqoridagi barcha funksiyalar uchun yagona handler
@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    """
    :param call: Handlerga kelgan Callback query
    :param callback_data: Tugma bosilganda kelgan ma'lumotlar
    """

    # Foydalanuvchi so'ragan Level (qavat)
    current_level = callback_data.get("level")

    # Foydalanuvchi so'ragan Kategoriya
    category = callback_data.get("category")

    # Ost-kategoriya (har doim ham bo'lavermaydi)
    subcategory = callback_data.get("subcategory")

    # Mahsulot ID raqami (har doim ham bo'lavermaydi)
    item_id = int(callback_data.get("item_id"))

    # Har bir Level (qavatga) mos funksiyalarni yozib chiqamiz
    levels = {
        "2": list_items,  # Mahsulotlarni qaytaramiz
        "3": show_item,  # Mahsulotni ko'rsatamiz
    }

    # Foydalanuvchidan kelgan Level qiymatiga mos funksiyani chaqiramiz
    current_level_function = levels[current_level]

    # Tanlangan funksiyani chaqiramiz va kerakli parametrlarni uzatamiz
    await current_level_function(
        call, category=category, subcategory=subcategory, item_id=item_id
    )
