from aiogram import F
from aiogram.types import Message
from loader import dp
from bot.keyboards.default.items import get_items

@dp.message(F.text == '📦Mahsulotlar')
async def show_items(message: Message) -> None:
    items_keyboard = get_items()
    await message.answer('Mahsulotlar:', reply_markup=items_keyboard)
