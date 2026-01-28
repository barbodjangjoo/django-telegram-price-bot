from django.urls import path

from . import views

urlpatterns = [
    path('referrals/', views.create_referral_view, name='referrals'),
    path('users/upsert/', views.telegram_upsert_view, name='user-upsert'),
    # path('users/<int:telegram_id>/status/', views.)
]
