from django.core.management.base import BaseCommand
from bot.telegram_bot import start_bot

class Command(BaseCommand):
    help = 'Run Telegram Bot'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting Telegram Bot...'))
        start_bot()
