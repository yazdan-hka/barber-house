# Generated by Django 4.2 on 2023-05-29 20:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_alter_verification_expires_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verification',
            name='is_valid',
        ),
        migrations.AddField(
            model_name='verification',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='verification',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 30, 0, 22, 35, 793727)),
        ),
    ]
