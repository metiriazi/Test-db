from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import BOT_TOKEN

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "سلام 👋\n"
        "به ربات خوش اومدی."
    )


async def main():
    await dp.start_polling(bot)


if name == "main":
    import asyncio
    asyncio.run(main())
