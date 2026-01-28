from rest_framework import serializers

from .models import TelegramUser


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = [
            'id',
            'telegram_id',
            'username',
            'first_name',
            'user',
            'referred_by',
            'created_at',
            'updated_at',
        ]

class TelegramUpsertSerializer(serializers.Serializer):
    telegram_id = serializers.IntegerField()
    username = serializers.CharField(required=False, allow_blank=True)
    first_name = serializers.CharField(required=False, allow_blank=True)