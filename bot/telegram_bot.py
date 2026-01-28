import os
from telegram.ext import ApplicationBuilder, CommandHandler
from bot.handlers.start import start
from bot.handlers.my_status import my_status
from bot.handlers.ref_summary import ref_summary

BOT_TOKEN = os.environ.get("BOT_TOKEN")

def start_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("my_status", my_status))
    app.add_handler(CommandHandler("ref_summary", ref_summary))
    print("Bot is running...")
    app.run_polling()
