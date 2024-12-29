from django.core.exceptions import ValidationError
from .models import *


# --- type --- #
def type_name(value):
    if Types.objects.filter(name=value).exists():
        raise ValidationError("Bunday ma'lumot allaqachon qo'shilgan.")
    elif len(value) < 5:
        raise ValidationError("Tur nomi kamida 5 ta belgidan iborat bo'lishi kerak.")

# --- register --- #
def user_valid(value):
    if User.objects.filter(username=value).exists():
        raise ValidationError(
            "Bu foydalanuvchi nomi allaqachon ro'yxatdan o'tgan. Iltimos, boshqa foydalanuvchi nomini tanlang.")