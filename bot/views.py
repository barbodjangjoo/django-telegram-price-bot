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