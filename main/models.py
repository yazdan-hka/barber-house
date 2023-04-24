from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
# from django.urls import reverse
# from django.contrib.auth.models import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from datetime import timedelta, datetime
import secrets
# Create your models here.

types = (
    ('c', 'braider'),
    ('b', 'customer')
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
    user_name = models.CharField(max_length=27, null=False, unique=True)
    email = models.EmailField(max_length=252, null=False, unique=True)
    password = models.CharField(max_length=126, validators=[], null=False)
    phone_number = PhoneNumberField(default='No Number.', null=True, unique=True)
    last_login = models.DateTimeField(null=True, blank=True)
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)


    # def clean(self):

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    def update_last_login(self):
        self.last_login = datetime.now()
    def save(self, update_fields=None):
        # Inserting value to last login

        self.update_last_login()
        # generate a token for a given user

        token = secrets.token_urlsafe(32)
        verification = Verification(token=token, rel=self)
        # Hash the password before saving the model

        self.password = make_password(self.password)
        super().save()
        # saving the generated token
        verification.save()


class Verification(models.Model):
    rel = models.ForeignKey(Braider, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=datetime.now()+timedelta(days=1))
    is_valid = models.BooleanField(default=True)
    # is_email_verified = models.BooleanField(default=False)
    # is_number_verified = models.BooleanField(dafault=False)

    def is_expired(self):
        return datetime.now() >= self.expires_at

    def save(self, *args, **kwargs):
        if self.is_expired():
            self.is_valid = False
        super(Verification, self).save(*args, **kwargs)


class PublicInfo(models.Model):
    rel = models.ForeignKey(Braider, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=23, null=False)
    last_name = models.CharField(max_length=22, null=False)
    user_type = models.CharField(max_length=8, choices=types, default='customer', null=False)
    biography = models.CharField(max_length=1024, null=True, blank=True)
    # error_messages = {'blank': ''}

class SocialMedia(models.Model):
    # validation for each must be provided.
    rel = models.ForeignKey(Braider, on_delete=models.CASCADE)
    instagram = models.CharField(max_length=30, unique=True, null=True, blank=True, error_messages={"unique":"Instagram ID already exists."})  # letter, number, underscore, period
    twitter = models.CharField(max_length=15, unique=True, null=True, blank=True)  # letter, number, underscore
    youtube = models.CharField(max_length=20, unique=True, null=True, blank=True)  # letter, number, space
    tiktok = models.CharField(max_length=24, unique=True, null=True, blank=True)  # letter, number, underscore, period
class LocationInfo(models.Model):
    rel = models.ForeignKey(Braider, on_delete=models.CASCADE)
    country = models.CharField(max_length=27, default='none', null=False)
    city = models.CharField(max_length=81, default='none', null=False)
    # location
class BusinessInfo(models.Model):
    rel = models.ForeignKey(Braider, on_delete=models.CASCADE)
    name = models.CharField(max_length=36, null=True)
    address = models.CharField(max_length=252, null=True)
    website = models.URLField(max_length=200, null=True)






    #
    # def __str__(self):
    #     value = self.country + '/' + self.city + ' ID: ' +self.user_name
    #     return value
    #

    #     self.save()
    # def is_authenticated(self):
    #     """
    #     Return True if the user is authenticated, else False.
    #     """
    #     return True if self.pk else False
    # def get_full_name(self):
    #     """
    #     Return the full name of the Braider
    #     """
    #     return f'{self.first_name} {self.last_name}'
    #
    # def get_short_name(self):
    #     """
    #     Return the short name of the Braider
    #     """
    #     return self.first_name
    #
    # def has_perm(self, perm, obj=None):
    #     """
    #     Return True if the Braider has the specified permission
    #     """
    #     return self.is_staff
    #
    # def has_module_perms(self, app_label):
    #     """
    #     Return True if the Braider has any permissions in the specified app
    #     """
    #     return self.is_staff
    #
    # def get_username(self):
    #     """
    #     Return True if the Braider has any permissions in the specified app
    #     """
    #     return self.is_staff






