from rest_framework.serializers import ModelSerializer
from .models import UserModel

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['email','password']