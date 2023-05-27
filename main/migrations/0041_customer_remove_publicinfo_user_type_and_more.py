# Generated by Django 4.2 on 2023-05-27 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_alter_post_braider_alter_post_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=27, unique=True)),
                ('email', models.EmailField(max_length=252, unique=True)),
                ('password', models.CharField(max_length=126)),
                ('first_name', models.CharField(max_length=23)),
                ('last_name', models.CharField(max_length=22)),
            ],
        ),
        migrations.RemoveField(
            model_name='publicinfo',
            name='user_type',
        ),
        migrations.AlterField(
            model_name='publicinfo',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pic.jpg', null=True, upload_to='profile-pictures/'),
        ),
        migrations.AlterField(
            model_name='verification',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 28, 18, 24, 21, 452455)),
        ),
    ]
