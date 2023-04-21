from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
# from django.urls import reverse
# from django.contrib.auth.models import auth
from django.contrib.auth.hashers import make_password, check_password


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

    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    user_name = models.CharField(max_length=70, null=False, unique=True)
    user_type = models.CharField(max_length=8, choices=types, default='customer', null=False)
    insta_id = models.CharField(max_length=40, default='braidstarz', null=False, unique=True)
    email = models.EmailField(max_length=256, null=False, unique=True)
    password = models.CharField(max_length=120, validators=[], null=False)
    phone_number = PhoneNumberField(default='No Number.', null=False, unique=True)
    country = models.CharField(max_length=50, default='none', null=False)
    city = models.CharField(max_length=50, default='none', null=False)
    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        value = self.country + '/' + self.city + ' ID: ' +self.user_name
        return value

    def save(self, update_fields=None):
        # Hash the password before saving the model
        self.password = make_password(self.password)
        print(update_fields)
        super().save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def update_last_login(self):
        self.last_login = timezone.now()

        self.save()

    def is_authenticated(self):
        """
        Return True if the user is authenticated, else False.
        """
        return True if self.pk else False

    #
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






