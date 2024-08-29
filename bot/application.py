from asyncio import run
import logging
import sys
from bot.utils.notify_admins import on_startup_notify
from bot.utils.set_bot_commands import set_default_commands
from loader import bot, dp


async def on_startup(dp):
    await on_startup_notify()
    await set_default_commands()


async def main() -> None:
    await dp.start_polling(bot, on_startup=on_startup)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    run(main())
