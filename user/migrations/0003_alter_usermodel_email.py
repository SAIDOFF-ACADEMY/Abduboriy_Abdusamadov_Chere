# Generated by Django 4.2.13 on 2024-07-10 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_usermodel_telegram_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermodel",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
