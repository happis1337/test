from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_info():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📢 Мой канал", url="https://t.me/happispython"),
                InlineKeyboardButton(text="💬 Мой лc", url="https://t.me/urvea"),
            ],
            [
                InlineKeyboardButton(text="🐙 Мой GitHub", url="https://github.com/happis1337"),
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return keyboard
