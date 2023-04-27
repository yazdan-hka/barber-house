# Generated by Django 4.2 on 2023-04-27 21:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_alter_verification_expires_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='braider',
            name='posted_pictures',
        ),
        migrations.AlterField(
            model_name='verification',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 29, 1, 57, 9, 813295)),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='posts/')),
                ('description', models.CharField(max_length=81)),
                ('category', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('braider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='main.braider')),
            ],
        ),
    ]
