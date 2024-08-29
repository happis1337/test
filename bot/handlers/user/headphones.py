from aiogram import F
from aiogram.types import Message
from loader import dp


@dp.message(F.text == '🎧Headphones')
async def show_items(message: Message) -> None:
    photo_url = 'https://avatars.mds.yandex.net/get-mpic/12216141/2a000001906e50d937e68f0766fb64031184/900x1200'

    my_headphones = '''
🎧 MSI DS502 Gaming Headphones - это ваш ключ к победе! 🏆
💰Price: 57$
🎧7.1 surround sound
💥мощный звук 
🛋️удобные амбушюры
'''

    await message.answer_photo(photo=photo_url, caption=my_headphones)
