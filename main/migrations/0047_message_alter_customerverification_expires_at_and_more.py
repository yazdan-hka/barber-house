# Generated by Django 4.2 on 2023-06-11 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_alter_verification_expires_at_customerverification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=33)),
                ('email', models.EmailField(max_length=252)),
                ('message', models.CharField(max_length=512)),
            ],
        ),
        migrations.AlterField(
            model_name='customerverification',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 11, 12, 32, 44, 119889)),
        ),
        migrations.AlterField(
            model_name='verification',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 11, 12, 32, 44, 118889)),
        ),
    ]
