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
    
class TelegramUserStatusSerializer(serializers.ModelSerializer):
    referrer_telegram_id = serializers.SerializerMethodField()

    class Meta:
        model = TelegramUser
        fields = [
            "telegram_id",
            "created_at",
            "referrer_telegram_id",
        ]

    def get_referrer_telegram_id(self, obj):
        return obj.referred_by.telegram_id if obj.referred_by else None
    

class ReferralItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = (
            "telegram_id",
            "created_at",
        )
