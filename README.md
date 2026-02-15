Django Telegram Price Monitor is a Telegram bot created with Django and Celery that is capable of production use. It fetches and posts market prices to a Telegram channel using an external API. Some of the features included are:

Integration with Telegrma Bot API
Price monitoring with Celery
API failure retry
Dockerized app
Separated web, worker, and redis containers
Environment based configs The tech stack for this app includes the following:
Django and Django REST Framework
Celery
Redis
Docker and Docker Compose
Telegram Bot API

Architecture
Telegram User / Channel
        ↓
Telegram Bot
        ↓
Django API
        ↓
Celery Worker
        ↓
External Price API
        ↓
Database


1) Setup & Run
git clone https://github.com/yourusername/django-telegram-price-monitor.git
cd django-telegram-price-monitor

2) Create environment file:
cp .env.example .env

Fill in your Telegram bot token and channel ID.
3) Build and run containers:

docker-compose up --build

4)Run migrations:

docker-compose exec web python manage.py migrate
