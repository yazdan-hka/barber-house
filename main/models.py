from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib.auth.models import auth

# Create your models here.

types = (
    ('braider', 'braider'),
    ('customer', 'customer')
)


def validate_password(value):
    number = '0123456789'
    chars = 'abcdefghijklmnopqrstuvwxyz'
    cap_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    wi = '!@#$%^&*()_-+={[}]|\\?/>,<.:;'
    password = value

    num = False
    char = False
    cap = False
    wierd = False
    le = False
    stars = ''

    if len(password) >= 8:
        le = True
    for i in number:
        if i in password:
            num = True
    for i in chars:
        if i in password:
            char = True
    for i in cap_chars:
        if i in password:
            cap = True
    for i in wi:
        if i in password:
            wierd = True

    if num or char:
        stars = '*'
    if num and char:
        stars = '**'
    if char and cap:
        stars += '*'
    if wierd:
        stars += '*'
    if le:
        stars += '*'

    if stars != '*****':
        raise ValidationError('your password is week. are you sure you used capital and small letters, numbers, '
                              'and special characters in the length of 8 or more? '.title(),
                              params={'value': value})


class Braider(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    user_type = models.CharField(max_length=8, choices=types, default='customer')
    insta_id = models.CharField(max_length=40, default='braidstarz')
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=120, validators=[validate_password])
    phone_number = PhoneNumberField(default='No Number.')
    country = models.CharField(max_length=30, default='none')
    city = models.CharField(max_length=50, default='none')






