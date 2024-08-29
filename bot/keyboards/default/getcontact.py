from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_phone_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Share Contact", request_contact=True)
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    return keyboard
