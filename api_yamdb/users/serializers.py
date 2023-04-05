from django.core.validators import RegexValidator
from rest_framework import serializers

from .models import CustomUser, REGEX


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'username', 'bio', 'email', 'role',
        )


class ConfirmationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        validators=[RegexValidator(REGEX)],
    )
    email = serializers.EmailField(
        max_length=254,
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                "Использовать имя 'me' в качестве username запрещено.")
        return value


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'confirmation_code')
