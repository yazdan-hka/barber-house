from django.contrib.auth.backends import ModelBackend
from main.models import Braider


class BraiderBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Braider.objects.get(user_name=username)
        except Braider.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        else:
            return None
