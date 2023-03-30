# Generated by Django 2.2.20 on 2023-03-30 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20230330_2011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_pure_phone',
            new_name='pure_phone',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='owned_flats',
        ),
        migrations.AddField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(blank=True, related_name='owner_flats', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claim_flat', to='property.Flat', verbose_name='Претензия по квартире:'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claim_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь:'),
        ),
    ]