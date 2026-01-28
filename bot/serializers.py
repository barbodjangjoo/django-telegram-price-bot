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


class ReferralCreateSerializer(serializers.Serializer):
    referrer_telegram_id = serializers.IntegerField()
    referred_telegram_id = serializers.IntegerField()

    def validate(self, attrs):
        if attrs["referrer_telegram_id"] == attrs["referred_telegram_id"]:
            raise serializers.ValidationError(
                "Referrer and referred cannot be the same"
            )
        return attrs