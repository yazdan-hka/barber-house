from django.db import models
from main.models import Braider

# Create your models here.


# class PostedMedia(models.Model):
#     braider = models.ForeignKey(Braider, on_delete=models.CASCADE, related_name='posted_media')
#     description = models.CharField(max_length=81)
#     category = models.CharField(max_length=40)
#     image = models.ImageField(upload_to='posted-pictures')
#     def __str__(self):
#         return self.braider + ' ' + self.category