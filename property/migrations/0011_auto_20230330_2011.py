# Generated by Django 2.2.20 on 2023-03-30 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20230330_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flat', to='property.Flat', verbose_name='Претензия по квартире:'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь:'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='Лайки'),
        ),
    ]
