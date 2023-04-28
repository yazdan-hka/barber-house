from django.contrib import admin
from .models import Braider, PublicInfo, SocialMedia, Post, LocationInfo, Verification, BusinessInfo

# Register your models here.
admin.site.register(Braider)
admin.site.register(PublicInfo)
admin.site.register(SocialMedia)
admin.site.register(Post)
admin.site.register(LocationInfo)
admin.site.register(Verification)
admin.site.register(BusinessInfo)
