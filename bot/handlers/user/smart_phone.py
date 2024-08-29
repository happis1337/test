from aiogram import F
from aiogram.types import Message
from loader import dp


@dp.message(F.text == '📱Smartphone')
async def show_items(message: Message) -> None:
    photo_url = 'https://fdn2.gsmarena.com/vv/pics/asus/asus-rog-phone-8-pro-1.jpg'

    my_phone = '''
📛Asus rog phone 9 pro
💰96403.69₽

Network & Availability: 

📱 Network Technology: GSM / CDMA / HSPA / LTE / 5G ⚡️
🚀 Launch: Announced 🗓️ 2024, January 08
✅ Status: Available. Released 🗓️ 2024, January 18

Design & Build:

📏 Dimensions: 163.8 x 76.8 x 8.9 mm (6.45 x 3.02 x 0.35 in)
⚖️ Weight: 225 g (7.94 oz)
✨ Build: Glass front (Gorilla Glass Victus 2) 💎, glass back (Gorilla Glass) 💎, aluminum frame 
🔐 SIM: Dual SIM (Nano-SIM, dual stand-by) 
💧 Protection: IP68 dust/water resistant (up to 1.5m for 30 min) 💦
💡 Special Features: 341 Mini-LED programmable matrix (on the back) 🎆, Pressure sensitive zones (Gaming triggers) 🕹️

Performance:

🤖 OS: Android 14, up to 2 major Android upgrades 
🧠 Chipset: Qualcomm SM8650-AB Snapdragon 8 Gen 3 (4 nm) 
⚡️ CPU: Octa-core (1x3.3 GHz Cortex-X4 & 3x3.2 GHz Cortex-A720 & 2x3.0 GHz Cortex-A720 & 2x2.3 GHz Cortex-A520) 
🚀 GPU: Adreno 750 
💾 Memory: 
    * Internal: 512GB 16GB RAM, 1TB 24GB RAM 
    * Card slot: No 🚫
    * Storage: UFS 4.0, NTFS support for external storage 
'''

    await message.answer_photo(photo=photo_url, caption=my_phone)
