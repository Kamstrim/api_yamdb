from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import UniqueConstraint
from users.models import User


class Review(models.Model):
    """Модель для отзывов"""
    text = models.TextField(
        help_text="Напишите текст отзыва",
    )
    score = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1, "Минимальная оценка - 1"),
            MaxValueValidator(10, "Максимальная оценка - 10"),
        ],
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    class Meta:
        ordering = ("-pub_date",)
        constraints = [
            UniqueConstraint(
                fields=['author', 'title'],
                name='unique_review')
        ]

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Модель для комментариев"""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="author",
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        auto_now_add=True,
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    class Meta:
        ordering = ("-pub_date",)

    def __str__(self):
        return self.text
