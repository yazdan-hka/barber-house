# Generated by Django 4.2 on 2023-05-28 15:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_customer_remove_publicinfo_user_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 29, 19, 4, 43, 841150)),
        ),
    ]
