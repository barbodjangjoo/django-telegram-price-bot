import os
from telegram.ext import ApplicationBuilder, CommandHandler
from bot.handlers.start import start

BOT_TOKEN = os.environ.get("BOT_TOKEN")

def start_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()
