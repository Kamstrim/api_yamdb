from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

REGEX = '^[\w.@+-]+\Z'


class CustomUser(AbstractUser):
    USER = 'US'
    MODERATOR = 'MD'
    ADMIN = 'AD'
    ROLE_CHOICES = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    ]
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[RegexValidator(REGEX)]
    )
    email = models.EmailField(
        max_length=256,
        unique=True,
    )

    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        max_length=2,
        choices=ROLE_CHOICES,
        default=USER,
    )
