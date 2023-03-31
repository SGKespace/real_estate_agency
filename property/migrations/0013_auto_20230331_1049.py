# Generated by Django 2.2.20 on 2023-03-31 07:49

from django.db import migrations

def migrate_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        owner_flats = Owner.objects.filter(name=flat.owner, phonenumber=flat.owners_phonenumber)
        flat.owner_flats.set(owner_flats)



class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20230330_2100'),
    ]

    operations = [
        migrations.RunPython(migrate_owners)
    ]
