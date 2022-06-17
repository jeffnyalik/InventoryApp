from pkg_resources import require
from rest_framework import serializers
from .models import Roles, CustomUser

class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    fullName = serializers.CharField()
    role = serializers.ChoiceField(Roles)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(required=False)
    is_new_user = serializers.BooleanField(required=False, default=False)


class UpdatePasswordSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    password = serializers.CharField()


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ("password")
