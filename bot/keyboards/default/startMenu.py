from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_keyboard():
    keyboard = [
        [
            KeyboardButton(text="📦Mahsulotlar"),
            KeyboardButton(text="👤Shaxsiy kabinet")
        ],
        [
            KeyboardButton(text="ℹ️Men xaqimda")
        ]
    ]

    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
