# Generated by Django 4.2 on 2023-04-18 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_braider_city_braider_cityd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='braider',
            name='cityd',
        ),
        migrations.AddField(
            model_name='braider',
            name='city',
            field=models.CharField(default='none', max_length=50),
        ),
    ]
