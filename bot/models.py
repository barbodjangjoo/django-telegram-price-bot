from django.db import models
from django.contrib.auth import get_user_model

class TelegramUser(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)

    user = models.OneToOneField(get_user_model(),null=True,blank=True,on_delete=models.SET_NULL)

    referred_by = models.ForeignKey("self",null=True,blank=True,on_delete=models.SET_NULL,related_name="referrals")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PriceLog(models.Model):
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
