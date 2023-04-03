from rest_framework import serializers

from .models import CustomUser


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'username', 'bio', 'email', 'role',
        )

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError("Нельзя использовать имя 'me' ")
        return value


class ConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'confirmation_code')
