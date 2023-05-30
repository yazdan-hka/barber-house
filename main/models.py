import secrets
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from datetime import timedelta, datetime
from django.core.validators import FileExtensionValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
# Create your models here.

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


class Customer(models.Model):
    user_name = models.CharField(max_length=27, null=False, unique=True)
    email = models.EmailField(max_length=252, null=False, unique=True)
    password = models.CharField(max_length=126, validators=[], null=False)
    first_name = models.CharField(max_length=23, null=False)
    last_name = models.CharField(max_length=22, null=False)

    def check_pass(self, raw_password):
        return check_password(raw_password, self.password)

    def save(self, update_fields=None):

        token = secrets.token_urlsafe(32)
        verification = CustomerVerification(token=token, rel=self)

        if 'pbkdf2_sha256$' not in self.password:
            self.password = make_password(self.password)

        super().save()
        verification.save()

class Braider(models.Model):
    user_name = models.CharField(max_length=27, null=False, unique=True)
    email = models.EmailField(max_length=252, null=False, unique=True)
    password = models.CharField(max_length=126, validators=[], null=False)
    phone_number = PhoneNumberField(default='No Number.', null=True, unique=True)
    show_phone = models.BooleanField(default=False)
    show_email = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    # posted_pictures = models.ImageField(
    #     upload_to='posted-pictures/',
    #     default='posted_media.jpg',
    #     null=True,
    #     validators=[
    #         FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
    #         MaxValueValidator(512000),
    #     ]
    # )
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)

    def __str__(self):
        return f'braider {self.user_name} from: {self.locationinfo.country}, {self.locationinfo.city}'
    def is_authenticated(self):
        # Return True if the user is authenticated, else False.
        return True if self.pk else False
    def check_pass(self, raw_password):
        return check_password(raw_password, self.password)
    def update_last_login(self):
        self.last_login = datetime.now()
    def save(self, update_fields=None):

        self.update_last_login()

        token = secrets.token_urlsafe(32)
        verification = Verification(token=token, rel=self)

        if 'pbkdf2_sha256$' not in self.password:
            self.password = make_password(self.password)

        super().save()
        verification.save()
class Post(models.Model):
    braider = models.ForeignKey(Braider, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='posts/', null=False, error_messages={'blank': 'you cannot post a picture without the picture itself. right?'.title()})
    description = models.CharField(max_length=81, null=True)
    category = models.CharField(max_length=40, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.description}'
class Verification(models.Model):
    rel = models.ForeignKey(Braider, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=datetime.now()+timedelta(minutes=9))
    is_email_verified = models.BooleanField(default=False)
    # is_number_verified = models.BooleanField(default=False)

    def is_expired(self):
        time = datetime.now()
        time = timezone.make_aware(time)
        return time >= self.expires_at

    def save(self, *args, **kwargs):
        self.expires_at = datetime.now()+timedelta(minutes=9)
        super(Verification, self).save(*args, **kwargs)

class CustomerVerification(models.Model):
    rel = models.ForeignKey(Customer, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=datetime.now() + timedelta(minutes=9))
    is_email_verified = models.BooleanField(default=False)

    # is_number_verified = models.BooleanField(default=False)

    def is_expired(self):
        time = datetime.now()
        time = timezone.make_aware(time)
        return time >= self.expires_at

    def save(self, *args, **kwargs):
        self.expires_at = datetime.now() + timedelta(minutes=9)
        super(CustomerVerification, self).save(*args, **kwargs)

class PublicInfo(models.Model):
    rel = models.OneToOneField(Braider, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=23, null=False)
    last_name = models.CharField(max_length=22, null=False)
    biography = models.CharField(max_length=1024, null=True, blank=True, error_messages={'blank': 'are you serious?'})
    profile_picture = models.ImageField(
        upload_to='profile-pictures/',
        default='profile_pic.jpg',
        null=True,
        blank=True,
        validators=[
            # FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            # MaxValueValidator(512000),
        ]
    )

class SocialMedia(models.Model):
    # validation for each must be provided.
    rel = models.OneToOneField(Braider, on_delete=models.CASCADE)
    instagram = models.CharField(max_length=234, unique=True, null=True, blank=True, error_messages={"unique":"Instagram ID already exists."})  # letter, number, underscore, period
    twitter = models.CharField(max_length=234, unique=True, null=True, blank=True, error_messages={"unique":"Twitter ID already exists."})  # letter, number, underscore
    facebook = models.CharField(max_length=234, unique=True, null=True, blank=True, error_messages={"unique":"Facebook ID already exists."})  # letter, number, underscore
    youtube = models.CharField(max_length=234, unique=True, null=True, blank=True, error_messages={"unique":"Youtube ID already exists."})  # letter, number, space
    tiktok = models.CharField(max_length=234, unique=True, null=True, blank=True, error_messages={"unique":"Tiktok ID already exists."})  # letter, number, underscore, period
class LocationInfo(models.Model):
    rel = models.OneToOneField(Braider, on_delete=models.CASCADE)
    country = models.CharField(max_length=27, default='none', null=False)
    city = models.CharField(max_length=81, default='none', null=False)
    # location
class BusinessInfo(models.Model):
    rel = models.OneToOneField(Braider, on_delete=models.CASCADE)
    name = models.CharField(max_length=81, null=True, blank=True)
    address = models.CharField(max_length=252, null=True, blank=True)
    website = models.URLField(max_length=234, null=True, blank=True)





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






