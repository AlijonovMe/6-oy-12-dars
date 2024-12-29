from django.core.exceptions import ValidationError
from .models import *


# --- course --- #
def course_name(value):
    if Course.objects.filter(name=value).exists():
        raise ValidationError("Bunday ma'lumot allaqachon qo'shilgan.")
    elif len(value) < 5:
        raise ValidationError("Kurs nomi kamida 5 ta belgidan iborat bo'lishi kerak.")


# --- lesson --- #
def lesson_name(value):
    if Lessons.objects.filter(name=value).exists():
        raise ValidationError("Bunday ma'lumot allaqachon qo'shilgan.")
    elif len(value) < 5:
        raise ValidationError("Dars nomi kamida 5 ta belgidan iborat bo'lishi kerak.")


def homework_length(value):
    length = len(value)
    if length < 5:
        raise ValidationError("Uyga vazifa matni kamida 5 ta belgidan iborat bo'lishi kerak.")
    elif length > 1000:
        raise ValidationError("Uyga vazifa matni uzunligi 1000 ta belgidan oshmasligi zarur.")


# --- register --- #
def user_valid(value):
    if User.objects.filter(username=value).exists():
        raise ValidationError(
            "Bu foydalanuvchi nomi allaqachon ro'yxatdan o'tgan. Iltimos, boshqa foydalanuvchi nomini tanlang.")