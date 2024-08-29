from aiogram import F
from aiogram.types import Message
from loader import dp
from bot.keyboards.inline.about import get_info


@dp.message(F.text == 'ℹ️Men xaqimda')
async def show_info(message: Message) -> None:
    info_keyboard = get_info()
    await message.answer('Me:', reply_markup=info_keyboard)
