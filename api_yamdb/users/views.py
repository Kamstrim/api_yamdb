from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import permission_classes, api_view, action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .exceptions import UserValueError
from .permissions import IsAdmin
from .models import CustomUser
from .serializers import UsersSerializer, ConfirmationSerializer, TokenSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def get_confirmation_code(request):
    """Создаем пользователя и отправляем код подтверждения"""
    serializer = ConfirmationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    username = serializer.data.get('username')
    user, created = CustomUser.objects.get_or_create(username=username, email=email)
    if not created:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        'Подтверждение доступа на api_yamdb',
        f'Ваш код подтверждения: {confirmation_code}',
        settings.AUTH_EMAIL,
        [email],
        fail_silently=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_jwt_token(request):
    """Получение Токена"""
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exceptions=True)
    user = get_object_or_404(
        CustomUser,
        username=serializer.data.get('username')
    )
    if not user:
        raise UserValueError('Ошибка имени пользователя')
    confirmation_code = serializer.data.get('confirmation_code')
    if not default_token_generator.check_token(user, confirmation_code):
        return Response(
            {'Код введен не верно'},
            status=status.HTTP_400_BAD_REQUEST
        )
    refresh = RefreshToken.for_user(user)
    return Response(
        {'access': str(refresh.access_token)},
        status=status.HTTP_200_OK
    )


class UsersViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer = UsersSerializer
    lookup_field = 'username'
    permission_classes = [IsAdmin]
    pagination_class = PageNumberPagination

    @action(
        detail=False,
        methods=['get', 'patch'],
        permission_classes=[IsAuthenticated]
    )
    def me(self, request):
        user = request.user
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exceptions=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

