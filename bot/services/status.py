from bot.models import TelegramUser

def get_user_status(telegram_id: int) -> dict:
    user = TelegramUser.objects.get(telegram_id=telegram_id)

    data = {
        "telegram_id": user.telegram_id,
        "referrer_id": user.referred_by.telegram_id if user.referred_by else None,
        "created_at": user.created_at,
        "is_referrer": user.referrals.exists(),
    }

    if data["is_referrer"]:
        referrals_qs = user.referrals.order_by("-created_at")

        data["referrals_count"] = referrals_qs.count()
        data["last_referrals"] = list(
            referrals_qs[:5].values("telegram_id", "created_at")
        )

    return data
