# Generated by Django 4.2.2 on 2023-06-14 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0002_calo_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calo',
            name='Calories',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='calo',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]