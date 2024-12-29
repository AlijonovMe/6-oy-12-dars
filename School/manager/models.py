from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nomi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sanasi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kurs "
        verbose_name_plural = "Kurslar"
        ordering = ['-id']


class Lessons(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nomi")
    homework = models.TextField(verbose_name="Uyga vazifa")
    deadline = models.DateTimeField(verbose_name="Uyga vazifa muddati")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sanasi")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan sanasi")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Kursi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Dars "
        verbose_name_plural = "Darslar"
        ordering = ['-id']

class Comment(models.Model):
    text = models.TextField(max_length=1000, verbose_name="Matni")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Muallif")
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, verbose_name="Dars")
    created = models.DateTimeField(auto_now_add=models.CASCADE, verbose_name="Yaratilgan")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Izoh "
        verbose_name_plural = "Izohlar"
        ordering = ['-id']

