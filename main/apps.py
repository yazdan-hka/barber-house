from django.apps import AppConfig
from .models import Braider


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'


admin.site.register(Braider)