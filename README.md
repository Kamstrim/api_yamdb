# Проект YaMDb

Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории «Книги», «Фильмы», «Музыка», «Искусство» и другие. Также произведениям могут быть присвоены жанры. Создание и управление категориями, произведениями и жанрами осуществляется только администратором. Пользователи могут оставить к произведениям текстовые отзывы и оценить их по шкале от одного до десяти. Из пользовательских оценок формируется усреднённая оценка произведения — рейтинг. Присутствует возможность комментирования отзывов.

## Функционал API:

1. Рецензирование и оценка произведений. Выстраивание системы рейтингов.

2. Комментирование оставленных отзывов.

## **Разработчики**

### 1. [Дмитрий Семенов](https://github.com/Kamstrim) (тим-лид):

Разработка системы регистрации и аутентификации, прав доступа, работы с токеном, системы подтверждения через e-mail.

### 2. [Павел Бутаков](https://github.com/KottaPav):

Разработка моделей Categories, Genres, Titles, выгрузка БД из файлов формата .csv.

### 3. [Евгений Щетинин](https://github.com/Zmeuko):

Разработка моделей Review и Comments.

## **Стек технологий**

![](https://img.shields.io/badge/Python-3.9-yellowgreen)

![](https://img.shields.io/badge/Django-3.2-yellowgreen)

![](https://img.shields.io/badge/djangorestframework-3.12.4-yellowgreen)

![](https://img.shields.io/badge/djangorestframework--simplejwt-4.7.2-yellowgreen)

## **Как запустить проект**

1. Клонировать репозиторий через командную строку:

`git clone https://github.com/Kamstrim/api_yamdb.git`

1. Перейти в папку с проектом

`cd api_yamdb`

1. Cоздать и активировать виртуальное окружение:
- WIN:

`python -m venv venv`

`source venv/scripts/activate`

- MAC/Linux:

`python3.9 -m venv venv`

`source venv/bin/activate`

1. Установить зависимости из файла requirements.txt:
- WIN:

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

- MAC/Linux:

`python3.9 -m pip install --upgrade pip`

`pip install -r requirements.txt`

1. Перейти в корневую папку проекта:

`cd api_yamdb`

1. Выполнить миграции:
- WIN:

`python manage.py makemigrations`

`python manage.py migrate`

- MAC/Linux:

`python3 manage.py makemigrations`

`python3 manage.py migrate`

1. Запустить проект:
- WIN:

`python manage.py runserver`

- MAC/Linux:

`python3 manage.py runserver`

Примеры запросов и документация по ссылке ([http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/))
