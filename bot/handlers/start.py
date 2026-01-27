from telegram import Update
from telegram.ext import ContextTypes
from asgiref.sync import sync_to_async
from bot.services.referral import create_or_get_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_id = update.effective_user.id
    username = update.effective_user.username
    first_name = update.effective_user.first_name

    referral_code = context.args[0] if context.args else None

    user = await sync_to_async(create_or_get_user)(
        telegram_id=telegram_id,
        username=username,
        first_name=first_name,
        referral_code=referral_code
    )

    msg = f"سلام {user.first_name or user.username}! "
    if user.referred_by:
        msg += f"شما توسط {user.referred_by.first_name or user.referred_by.username} معرفی شدید."
    else:
        msg += "خوش آمدید!"

    await update.message.reply_text(msg)




