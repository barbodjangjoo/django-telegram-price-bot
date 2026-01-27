from bot.models import TelegramUser

def create_or_get_user(telegram_id, username=None, first_name=None, referral_code=None):
    """
    Create user from telegram with referal 
    """
    user, created = TelegramUser.objects.get_or_create(
        telegram_id=telegram_id,
        defaults={
            "username": username,
            "first_name": first_name
        }
    )

    if created and referral_code:
        try:
            ref_user = TelegramUser.objects.get(id=int(referral_code))
            user.referred_by = ref_user
            user.save()
        except TelegramUser.DoesNotExist:
            pass

    return user
