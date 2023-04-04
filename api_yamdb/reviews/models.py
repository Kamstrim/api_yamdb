from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name='Название категории',
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name', )
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'slug'], name='name_slug_unique_ctg')
        ]

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name='Название жанра'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('name', )
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'slug'], name='name_slug_unique_gnr')
        ]

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name='Название'
    )
    year = models.PositiveSmallIntegerField(
        db_index=True,
        verbose_name='Год выпуска'
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='category',
        verbose_name='Категория'
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='title_genre',
        verbose_name='Жанр',
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ('-year',)

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField(
        verbose_name='Отзыв'
    )
    score = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Минимальная оценка - 1"),
            MaxValueValidator(10, message="Максимальная оценка - 10"),
        ],
        verbose_name='Оценка'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name='Автор'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name='Произведение'
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-pub_date',)
        constraints = (
            models.UniqueConstraint(fields=('author', 'title'),
                                    name='unique_author_title'),
        )

    def __str__(self):
        return f'Произведение: {str(self.title)[:15]}, Автор: {self.author}'


class Comment(models.Model):
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name='Автор'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name='Отзыв'
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:15]