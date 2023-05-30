# Generated by Django 4.2 on 2023-05-30 10:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_remove_verification_is_valid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 30, 14, 16, 15, 785132)),
        ),
        migrations.CreateModel(
            name='CustomerVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField(default=datetime.datetime(2023, 5, 30, 14, 16, 15, 785132))),
                ('is_email_verified', models.BooleanField(default=False)),
                ('rel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customer')),
            ],
        ),
    ]
