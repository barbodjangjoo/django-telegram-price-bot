from django.urls import path

from . import views


urlpatterns = [
    path('referrals/', views.create_referral_view, name='create-referral'),
    path('users/upsert/', views.telegram_upsert_view, name='user-upsert'),
    path('users/<int:telegram_id>/status/',views.telegram_user_status_view,name='user-status'),
    path('referrals/referrer/<int:telegram_id>/summary/',views.referral_summary_view,name='referral-summary'),
]