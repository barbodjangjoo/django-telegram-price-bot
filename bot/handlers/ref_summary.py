from telegram import Update
from telegram.ext import ContextTypes
from bot.models import TelegramUser
from asgiref.sync import sync_to_async

async def ref_summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_id = update.effective_user.id

    try:
        user = await sync_to_async(TelegramUser.objects.get)(telegram_id=telegram_id)
    except TelegramUser.DoesNotExist:
        await update.message.reply_text("You have not signed up yet!")
        return

    # تعداد زیرمجموعه‌ها
    referrals_qs = user.referrals.all().order_by("-created_at")
    count = await sync_to_async(referrals_qs.count)()
    last_five = await sync_to_async(list)(referrals_qs[:5])

    msg = f"You have {count} referrals.\nLast 5 referrals:\n"
    for r in last_five:
        msg += f"- {r.telegram_id} | {r.created_at.strftime('%Y-%m-%d %H:%M')}\n"

    await update.message.reply_text(msg)
