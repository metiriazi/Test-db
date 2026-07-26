from aiohttp import web

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import (
    CommandStart, 
    F
)
from aiogram.webhook.aiohttp_server import (
    SimpleRequestHandler,
    setup_application
)

from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton
)



# =========================
# Config
# =========================

BOT_TOKEN = "8902169504:AAFVjB6AqLulHXpCBm6ojLo5eBaQv6oX9z0"

WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = "https://test-2dkc.onrender.com/webhook"

HOST = "0.0.0.0"
PORT = 10000

# =========================
# Bot
# =========================

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)

dp = Dispatcher()

# =========================
# Handlers
# =========================
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 جزوات"),
            KeyboardButton(text="🎥 ویدیوها")
        ],
        [
            KeyboardButton(text="ℹ️ درباره ما")
        ]
    ],
    resize_keyboard=True
)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "یکی از گزینه‌ها را انتخاب کنید:",
        reply_markup=main_keyboard
    )




# =========================
# Startup
# =========================

async def on_startup(bot: Bot):
    await bot.set_webhook(WEBHOOK_URL)
    print("Webhook Set")

# =========================
# Shutdown
# =========================

async def on_shutdown(bot: Bot):
    await bot.delete_webhook()
    print("Webhook Deleted")

# =========================
# Main
# =========================

def main():

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    app = web.Application()

    SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    ).register(
        app,
        path=WEBHOOK_PATH,
    )

    setup_application(app, dp, bot=bot)

    web.run_app(
        app,
        host=HOST,
        port=PORT,
    )


if __name__ == "__main__":
    main()
