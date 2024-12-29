from django.db import models
from django.contrib.auth.models import User

class Types(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nomi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Turlar "
        verbose_name_plural = "Turlar"
        ordering = ['-id']


class Flowers(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nomi")
    description = models.TextField(default="Ma'lumot qo'shilmadi.", verbose_name="Tavsifi")
    price = models.IntegerField(verbose_name="Narxi")
    count = models.IntegerField(default=0, verbose_name="Soni")
    published = models.BooleanField(default=False, verbose_name="Nashr etilgan")
    type = models.ForeignKey(Types, on_delete=models.CASCADE, verbose_name="Turi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Gullar "
        verbose_name_plural = "Gullar"
        ordering = ['-id']

class Comment(models.Model):
    text = models.TextField(max_length=1000, verbose_name="Matni")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Muallif")
    flower = models.ForeignKey(Flowers, on_delete=models.CASCADE, verbose_name="Gul turi")
    created = models.DateTimeField(auto_now_add=models.CASCADE, verbose_name="Yaratilgan")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Izoh "
        verbose_name_plural = "Izohlar"
        ordering = ['-id']
