# Generated by Django 4.2.2 on 2023-06-15 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0004_rename_calories_calo_calories'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Calo',
        ),
    ]