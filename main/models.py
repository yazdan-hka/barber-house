from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

COLOR_CHOICES = (
    ('braider','Braider'),
    ('customer', 'Customer'),

)


class Braider(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    user_type = models.CharField(max_length=8, choices=COLOR_CHOICES, default='customer')
    insta_id = models.CharField(max_length=40, default='braidstarz')
    email = models.EmailField()
    password = models.CharField(max_length=120)
    phone_number = PhoneNumberField(default='No Number.')
    country = models.CharField(max_length=30, default='none')
    city = models.CharField(max_length=50, default='none')

    def get_absolute_url(self):

        return "/profile/%i/" % self.id




