from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = 'US'
    MODERATOR = 'MD'
    ADMIN = 'AD'
    ROLE_CHOICES = [
            (USER, 'user'),
            (MODERATOR, 'moderator'),
            (ADMIN, 'admin'),
    ]
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        max_length=2,
        choices=ROLE_CHOICES,
        default=USER,
    )
