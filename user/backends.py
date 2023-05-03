from django.contrib.auth.backends import BaseBackend
from main.models import Braider
from django.contrib.auth.backends import ModelBackend


class BraiderBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            braider = Braider.objects.get(user_name=username)
        except Braider.DoesNotExist:
            return None

        if braider.check_pass(password):
            return braider

        return None

    def user_can_authenticate(self, user):
        return True if user.is_active else False

    def is_authenticated(self, request, **kwargs):
        if request.user.is_authenticated:
            return True
        else:
            return False

    def get_user(self, user_id):
        try:
            return Braider.objects.get(pk=user_id)
        except Braider.DoesNotExist:
            return None


class CustomBackend(ModelBackend):
    def update_last_login(self, request, user):
        """
        Update the last_login date for the user
        """
        user.last_login = timezone.now()
        user.save()