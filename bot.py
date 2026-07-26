import asyncio
import os

from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

BOT_TOKEN = os.getenv("BOT_TOKEN")

WEBHOOK_PATH = "/webhook"

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("سلام 👋 ربات با Webhook اجرا شده است.")


async def on_startup(bot: Bot):
    render_url = os.getenv("RENDER_EXTERNAL_URL")

    if render_url:
        await bot.set_webhook(f"{render_url}{WEBHOOK_PATH}")
        print("Webhook Set!")


async def on_shutdown(bot: Bot):
    await bot.delete_webhook()


def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    app = web.Application()

    SimpleRequestHandler(
        dispatcher=dp,
        bot=bot
    ).register(app, path=WEBHOOK_PATH)

    setup_application(app, dp, bot=bot)

    web.run_app(
        app,
        host="0.0.0.0",
        port=int(os.getenv("PORT", 10000))
    )


if __name__ == "__main__":
    main()
