# Generated by Django 4.2 on 2023-04-23 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_remove_braider_city_remove_braider_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 24, 20, 44, 39, 390812)),
        ),
    ]