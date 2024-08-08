from .models import UserModel
from django.contrib.auth.backends import BaseBackend


class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
