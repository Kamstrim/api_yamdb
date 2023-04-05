
README.md

Что это за проект: Yambd - это сайт для критиков творчества в любом его проявлении.

Какие задачи решает:

    Помогает молодым критикам заявить о себе.

Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/Kamstrim/api_yamdb.git

cd api_yamdb

Cоздать и активировать виртуальное окружение:

python3 -m venv venv

source venv/bin/activate

Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip

pip install -r requirements.txt

Выполнить миграции:

python3 manage.py migrate

Запустить проект:

python3 manage.py runserver
