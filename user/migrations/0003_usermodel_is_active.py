# Generated by Django 5.0.7 on 2024-08-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_usermodel_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
