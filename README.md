# Link_shorteners

Проект Link_shorteners — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Ключевые возможности сервиса
- Генерация коротких ссылок и связь их с исходными длинными ссылками
- Переадресация на исходный адрес при обращении к коротким ссылкам
- /api/id/ — POST-запрос на создание новой короткой ссылки;
- /api/id/<short_id>/ — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.

## Технологии
[![Python](https://img.shields.io/badge/-Python3.9-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/-Flask2.0-464646?style=flat&logo=Flask&logoColor=ffffff&color=043A6B)](https://www.djangoproject.com/)
[![Jinja2](https://img.shields.io/badge/-Jinja2-464646?style=flat&logo=Jinja&logoColor=ffffff&color=043A6B)](https://www.postgresql.org/)
[![REST](https://img.shields.io/badge/-REST-464646?style=flat&logo=REST&logoColor=ffffff&color=043A6B)](https://www.django-rest-framework.org/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy1.4-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=043A6B)](https://www.postgresql.org/)

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Tatiana314/Link_shorteners.git && cd Link_shorteners
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать файл настроек окружения:

```
touch .env
```

Заполнить его:

```
FLASK_APP=Link_shorteners
FLASK_ENV=production
DATABASE_URI=<sqlite:///db.sqlite3>
SECRET_KEY=<SECRET_KEY>
```

Создать базу данных:

```
flask db upgrade
```

Запустить:

```
flask run
```
Сервис будет доступен по адресу `http://localhost:5000/`.

## Автор
[Мусатова Татьяна](https://github.com/Tatiana314)
