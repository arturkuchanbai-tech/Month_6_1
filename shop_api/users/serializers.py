from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from users.confirmation import verify_code
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import CustomUser


CustomUser = get_user_model()


class OauthSerializer(serializers.Serializer):
    code = serializers.CharField()


class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        token["last_login"] = user.last_login
        token["is_staff"] = user.is_staff
        token["call_me"] = "+996777777777"
        return token


class UserBaseSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=150)
    password = serializers.CharField()


class AuthValidateSerializer(UserBaseSerializer):
    pass


class RegisterValidateSerializer(UserBaseSerializer):
    def validate_username(self, email):
        try:
            CustomUser.objects.get(email=email)
        except:
            return email
        raise ValidationError("CustomUser уже существует!")


class ConfirmationSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    code = serializers.CharField(max_length=6)

    def validate(self, attrs):
        user_id = attrs.get("user_id")
        code = attrs.get("code")

        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise ValidationError("Пользователь не существует!")
        if not verify_code(user.id, code):
            raise ValidationError("Неверный или истёкший код!")
        user.is_active = True
        user.save()

        return attrs