from django.shortcuts import get_object_or_404
from rest_framework import serializers
from reviews.models import Comment, Review, Title
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer


from reviews.models import Category, Genre, Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
    )
    title = serializers.SlugRelatedField(
        slug_field="id",
        many=False,
        read_only=True
    )

    class Meta:
        fields = "__all__"
        model = Review

    def validate(self, data):
        if self.context["request"].method != "POST":
            return data
        title = get_object_or_404(
            Title,
            pk=self.context["view"].kwargs.get("title_id")
        )
        author = self.context["request"].user
        if Review.objects.filter(title_id=title, author=author).exists():
            raise serializers.ValidationError(
                "На данное произведение уже есть отзыв от Вас, спасибо!)"
            )
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username"
    )
    review = serializers.SlugRelatedField(read_only=True, slug_field="text")

    class Meta:
        fields = "__all__"
        model = Comment


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['slug']


class GenreSerializer(ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'
        read_only_fields = ['slug']


class TitleSerializer(ModelSerializer):
    categoty = SlugRelatedField(
        slug_field="id", queryset=Genre.objects.all()
    )
    genre = SlugRelatedField(
        slug_field="id", queryset=Genre.objects.all(), required=False
    )

    class Meta:
        model = Title
        fields = '__all__'
        read_only_fields = ['title_id']

