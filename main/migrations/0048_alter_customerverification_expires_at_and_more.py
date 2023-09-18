# Generated by Django 4.2.1 on 2023-07-19 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0047_message_alter_customerverification_expires_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customerverification",
            name="expires_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 19, 15, 33, 23, 906757)
            ),
        ),
        migrations.AlterField(
            model_name="verification",
            name="expires_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 19, 15, 33, 23, 906046)
            ),
        ),
    ]