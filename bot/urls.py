from django.urls import path

from . import views

urlpatterns = [
    path('users/upsert/', views.telegram_upsert_view, name='user-upsert'),
    
]
