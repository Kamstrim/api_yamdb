from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

REGEX = r'^[\w.@+-]+\Z'
LIMIT_USERNAME = 150
LIMIT_EMAIL = 254
LIMIT_ROLE = 50


class CustomUser(AbstractUser):
    """Кастомизация модели User."""

    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    ROLE_CHOICES = (
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    )
    username = models.CharField(
        max_length=LIMIT_USERNAME,
        validators=[RegexValidator(REGEX)],
        unique=True,
    )
    email = models.EmailField(
        max_length=LIMIT_EMAIL,
        unique=True,
    )

    bio = models.TextField(
        blank=True,
        null=True,
    )
    role = models.CharField(
        max_length=LIMIT_ROLE,
        choices=ROLE_CHOICES,
        default=USER
    )

    class Meta:
        ordering = ['-id']

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
