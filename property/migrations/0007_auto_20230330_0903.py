# Generated by Django 4.1.7 on 2023-03-30 06:03

import phonenumbers
from django.db import migrations

def normalize_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for number in Flat.objects.all():
        normal_phone = phonenumbers.parse(number.owners_phonenumber, "RU")
        if phonenumbers.is_valid_number(normal_phone):
            number.owner_pure_phone = normal_phone
            number.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_flat_owner_pure_phone_alter_flat_has_balcony_and_more'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers)
    ]