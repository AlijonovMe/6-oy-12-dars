# Generated by Django 5.1.3 on 2024-12-29 05:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_alter_lessons_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nomi'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, verbose_name='Matni')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Muallif')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.lessons', verbose_name='Dars')),
            ],
        ),
    ]