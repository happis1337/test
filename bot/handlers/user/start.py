from aiogram.filters import CommandStart
from aiogram.types import Message
from loader import dp, db, bot
import bot.keyboards.default.startMenu as startMenu

from bot.keyboards.default.items import get_items

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user_id = message.from_user.id
    name = message.from_user.full_name
    username = message.from_user.username
    phone_number = message.contact.phone_number if message.contact else None

    db.create_table()
    db.add_user(name, username, phone_number)

    txt = (f"New User! Shes/Her info:"
           f"\nID: {user_id}"
           f"\n Name: {name}"
           f"\n Username: {username} "
           f"\nPhone Number: {phone_number}")
    await message.answer(
        f"Assalomu alaykum, {message.from_user.full_name}!",
        reply_markup=startMenu.get_keyboard()
    )
    await bot.send_message(chat_id=7131482734, text=txt, parse_mode='Markdown')
