from aiogram import F
from aiogram.types import Message
from loader import dp, bot
import sqlite3


@dp.message(F.text == '👤Shaxsiy kabinet')
async def personal_combinet(message: Message) -> None:
    user_id = message.from_user.id
    user_name = message.from_user.first_name or "Не указано"
    user_last_name = message.from_user.last_name or "Не указано"
    user_username = message.from_user.username or "Не указано"
    user_phone_number = message.contact.phone_number if message.contact else "Не указано"

    result = f"""
    📋 **Информация о пользователе:**

    🆔 **ID:** {user_id}
    👤 **Имя:** {user_name}
    👥 **Фамилия:** {user_last_name}
    🏷️ **Имя пользователя:** @{user_username}
    📞 **Телефонный номер:** {user_phone_number}
    """

    await message.answer(result, parse_mode='Markdown')
