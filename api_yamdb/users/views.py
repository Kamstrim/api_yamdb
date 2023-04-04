from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, filters
from rest_framework.decorators import permission_classes, api_view, action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from .permissions import IsAdmin
from .models import CustomUser
from .serializers import (ConfirmationSerializer,
                          TokenSerializer, CustomUserSerializer
                          )


@api_view(['POST'])
@permission_classes([AllowAny])
def get_confirmation_code(request):
    """Создаем пользователя и отправляем код подтверждения"""
    serializer = ConfirmationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    username = serializer.data.get('username')
    user, created = CustomUser.objects.get_or_create(
        username=username,
        email=email
    )
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        'Подтверждение доступа на api_yamdb',
        f'Ваш код подтверждения: {confirmation_code}',
        settings.AUTH_EMAIL,
        [email]
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_jwt_token(request):
    """Получение Токена"""
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(
        CustomUser,
        username=request.data.get('username')
    )
    confirmation_code = request.data.get('confirmation_code')
    if not default_token_generator.check_token(
            user,
            confirmation_code
    ):
        return Response(
            {'Код введен не верно'},
            status=status.HTTP_400_BAD_REQUEST
        )
    token = AccessToken.for_user(user)
    return Response(
        {'token': str(token)},
        status=status.HTTP_200_OK
    )


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'username'
    permission_classes = [IsAdmin]
    http_method_names = ('get', 'post', 'delete', 'patch')
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)

    @action(
        detail=False,
        methods=['get', 'patch'],
        permission_classes=[IsAuthenticated]
    )
    def me(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        if request.method == 'PATCH':
            serializer = self.get_serializer(
                user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save(email=user.email, role=user.role)
        return Response(serializer.data, status=status.HTTP_200_OK)
