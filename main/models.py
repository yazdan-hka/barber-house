from django.db import models

# Create your models here.

COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)


class Braider(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    user_type = models.CharField(max_length=8, choices=COLOR_CHOICES, default='green')
    insta_id = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=120)
    number = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=50)






