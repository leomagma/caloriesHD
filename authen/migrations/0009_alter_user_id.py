# Generated by Django 4.2.2 on 2023-06-15 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0008_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
