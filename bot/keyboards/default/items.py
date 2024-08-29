from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_items():
    keyboard = [
        [
            KeyboardButton(text="📱Smartphone"),
            KeyboardButton(text="💻Laptop")
        ],
        [
            KeyboardButton(text="🎧Headphones")
        ]
    ]

    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
