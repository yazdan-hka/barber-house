# Generated by Django 4.2 on 2023-04-24 06:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_alter_verification_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessinfo',
            name='address',
            field=models.CharField(max_length=252, null=True),
        ),
        migrations.AlterField(
            model_name='businessinfo',
            name='name',
            field=models.CharField(max_length=36, null=True),
        ),
        migrations.AlterField(
            model_name='publicinfo',
            name='biography',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='insta',
            field=models.CharField(default='braidstarz', max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='tiktok',
            field=models.CharField(default='braidstarz', max_length=24, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='twitter',
            field=models.CharField(default='braidstarz', max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='youtube',
            field=models.CharField(default='braidstarz', max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='verification',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 25, 10, 30, 41, 221943)),
        ),
    ]
