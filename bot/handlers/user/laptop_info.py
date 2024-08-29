from aiogram import F
from aiogram.types import Message
from loader import dp


@dp.message(F.text == '💻Laptop')
async def show_items(message: Message) -> None:
    photo_url = 'https://img.telemart.ua/508264-648662-product_popup/msi-stealth-studio-14-a13ve-054xua-pure-white.png'

    my_laptop = """
📛MSI Stealth Studio 14 (A13VE-054XUA) Black-White
💰Price: 67 999₴
💻Description:
➕Процессор Intel Core 13-го поколения
Новейший процессор Intel Core 13-го поколения наделяет этот ноутбук великолепной 
производительностью при запуске ресурсоемких игр и работе в многозадачном режиме.

➕Видеокарта NVIDIA 40-серии

Видеокарты NVIDIA серии GeForce RTX 40 для ноутбуков используются в самых быстрых устройствах для игр 
и творческой работы. Детализированные виртуальные миры с трассировкой лучей и гигантский прорыв с точки зрения 
производительности посредством интеллектуальной технологии NVIDIA DLSS 3 – все это доступно благодаря высокоэффективной 
архитектуре NVIDIA Ada Lovelace. Кроме того, в этих видеокартах реализован комплекс технологий Max-Q
оптимизирующих энергопотребление, производительность, уровень шума и время автономной работы.
    """

    await message.answer_photo(photo=photo_url, caption=my_laptop)
