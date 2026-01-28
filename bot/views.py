from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import TelegramUser
from . import serializers

@api_view(['POST'])
def telegram_upsert_view(request):
    serializer = serializers.TelegramUpsertSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    data = serializer.validated_data

    user, created = TelegramUser.objects.get_or_create(
        telegram_id=data["telegram_id"],
        defaults={
            "username": data.get("username"),
            "first_name": data.get("first_name"),
        }
    )

    return Response(
        serializers.TelegramUserSerializer(user).data,
        status=status.HTTP_201_CREATED if created else status.HTTP_200_OK
    )

@api_view(['POST'])
def create_referral_view(request):
    serializer = serializers.ReferralCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    referrer_tid = serializer.validated_data["referrer_telegram_id"]
    referred_tid = serializer.validated_data["referred_telegram_id"]

    referrer, _ = TelegramUser.objects.get_or_create(
        telegram_id=referrer_tid
    )
    referred, _ = TelegramUser.objects.get_or_create(
        telegram_id=referred_tid
    )

    if referred.referred_by is not None:
        return Response(
            {"detail": "User already has a referrer"},
            status=status.HTTP_409_CONFLICT
        )

    referred.referred_by = referrer
    referred.save(update_fields=["referred_by"])

    return Response({
        "referrer_telegram_id": referrer.telegram_id,
        "referred_telegram_id": referred.telegram_id,
        "created_at": referred.updated_at
    }, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def telegram_user_status_view(request, telegram_id):
    user = get_object_or_404(
        TelegramUser.objects.select_related("referred_by"),
        telegram_id=telegram_id
    )

    serializer = serializers.TelegramUserStatusSerializer(user)
    return Response(serializer.data)

@api_view(["GET"])
def referral_summary_view(request, telegram_id):
    referrer = get_object_or_404(
        TelegramUser,
        telegram_id=telegram_id
    )

    referrals_qs = referrer.referrals.order_by("-created_at")

    return Response({
        "count": referrals_qs.count(),
        "last_5_referrals": serializers.ReferralItemSerializer(
            referrals_qs[:5],
            many=True
        ).data
    })