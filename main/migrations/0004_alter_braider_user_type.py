# Generated by Django 4.2 on 2023-04-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_braider_number_braider_city_braider_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='braider',
            name='user_type',
            field=models.CharField(choices=[('braider', 'Braider'), ('customer', 'Customer')], default='customer', max_length=8),
        ),
    ]
