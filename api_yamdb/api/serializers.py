from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer


from reviews.models import Category, Genre, Title


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

# 29 и 32 id ли там нужен?
