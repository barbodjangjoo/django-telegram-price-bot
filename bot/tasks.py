import requests
import os
from celery import shared_task
from django.utils import timezone

from .models import PriceLog

TELEGRAM_BOT_TOKEN = os.environ.get('BOT_TOKEN')
TELEGRAM_CHAT_ID= os.environ.get("CHANNEL_ID")
NAVASAN_API_URL=os.environ.get('API_URL')



@shared_task
def check_price():
    try:
        response = requests.get(NAVASAN_API_URL)
        response.raise_for_status()
        data = response.json()

        current_price = float(data['harat_naghdi_buy']['value'])

        last_price_record = PriceLog.objects.order_by('-created_at').first()
        last_price = last_price_record.value if last_price_record else current_price

        change_percent = abs((current_price - last_price) / last_price) * 100

        PriceLog.objects.create(value=current_price)

        if change_percent > 1:
            msg = f"⚡ Gold price changed: {current_price} ({change_percent:.2f}%)"
            requests.post(
                f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage',
                data={'chat_id': TELEGRAM_CHAT_ID, 'text': msg}
            )
        else:
            print(f"[{timezone.now()}] Change less than 1%: {current_price}")

    except Exception as e:
        print(f"[{timezone.now()}] Error fetching price or sending message: {e}")