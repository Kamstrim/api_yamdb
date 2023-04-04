from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from rest_framework.validators import UniqueValidator

REGEX = r'^[\w.@+-]+\Z'


class CustomUser(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    ROLE_CHOICES = (
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    )
    username = models.CharField(
        max_length=150,
        blank=False,
        validators=[RegexValidator(REGEX)],
        unique=True,
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
    )

    bio = models.TextField(
        blank=True,
        null=True,
    )
    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default=USER
    )

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = self.ADMIN
        super(CustomUser, self).save(*args, **kwargs)

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR
