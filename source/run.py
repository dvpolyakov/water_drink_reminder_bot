import logging
from aiogram import Bot, Dispatcher, ParseMode
# from aiogram.types import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

API_TOKEN = "6651361716:AAHNQThVpwYIr_4hlN8Ejo_9ea3TXePaQQg"
USER_ID = "219196569"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def send_drink_water_reminder():
    current_hour = datetime.now().hour
    if 10 <= current_hour < 18:
        await bot.send_message(
            USER_ID, "Time to drink a glass of water!", parse_mode=ParseMode.MARKDOWN
        )


async def on_startup(dp):
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_drink_water_reminder, "interval", minutes=10)
    scheduler.start()


async def on_shutdown(dp):
    await bot.send_message(USER_ID, "Bot is shutting down!")


if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
