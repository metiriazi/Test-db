from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

bot = Bot("YOUR_TOKEN")
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("سلام 🌹")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
