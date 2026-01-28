from telegram import Update
from telegram.ext import ContextTypes
from asgiref.sync import sync_to_async

from bot.services.status import get_user_status

@sync_to_async
def _get_status(telegram_id):
    return get_user_status(telegram_id)

async def my_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_id = update.effective_user.id
    status = await _get_status(telegram_id)

    msg = (
        f"📌 Your status:\n"
        f"🆔 Telegram ID: {status['telegram_id']}\n"
        f"👤 Referrer ID: {status['referrer_id']}\n"
        f"📅 Joined date: {status['created_at']:%Y-%m-%d %H:%M}\n"
    )

    if status["is_referrer"]:
        msg += f"\n👥 referrals : {status['referrals_count']}\n"
        msg += "lastest ref:\n"

        for ref in status["last_referrals"]:
            msg += f"- {ref['telegram_id']} | {ref['created_at']:%Y-%m-%d}\n"

    await update.message.reply_text(msg)
