import csv
from django.core.management.base import BaseCommand
from ...models import Category, Comment, Genre, Review, Title, User


class Command(BaseCommand):
    help = 'Импорт данных из csv файлов'

    def handle(self, *args, **options):
        datadicts = [["..../api_yamdb/static/data/category.csv", Category],
                     ["..../api_yamdb/static/data/comments.csv", Comment],
                     ["..../api_yamdb/static/data/genre_title.csv", Genre],
                     ["..../api_yamdb/static/data/genre.csv", Genre],
                     ["..../api_yamdb/static/data/review.csv", Review],
                     ["..../api_yamdb/static/data/titles.csv", Title],
                     ["..../api_yamdb/static/data/users.csv", User],
                     ]
        for i in datadicts:
            with open(i[0], newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                for x in reader:
                    category_created = i[1].objects.update_or_create(
                        id=int(x[0]), name=x[1], slug=x[2])
                    comments_created = i[1].objects.update_or_create(
                        id=int(x[0]), review_id=x[1], text=x[2],
                        author=x[3], pub_date=x[4])
                    genre_title_created = i[1].objects.update_or_create(
                        id=int(x[0]), title_id=x[1], genre_id=x[2])
                    genre_created = i[1].objects.update_or_create(
                        id=int(x[0]), name=x[1], slug=x[2])
                    review_created = i[1].objects.update_or_create(
                        id=int(x[0]), title_id=x[1], text=x[2],
                        author=x[3], score=x[4], pub_date=x[5])
                    titles_created = i[1].objects.update_or_create(
                        id=int(x[0]), name=x[1], year=x[2], category=x[3])
                    users_created = i[1].objects.update_or_create(
                        id=int(x[0]), username=x[1], email=x[2],
                        role=x[3], bio=x[4], first_name=x[5], last_name=x[6])
