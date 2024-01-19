# Проект YaCut

Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Технологии
- Python 3.9
- Flask 2.0
- Jinja2 3.0
- SQLAlchemy 1.4

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Tatiana314/yacut.git
```

```
cd yacut
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
FLASK_APP=yacut
FLASK_ENV=production
DATABASE_URI=<sqlite:///db.sqlite3>
SECRET_KEY=<SECRET_KEY>
```

Создать миграции:

```
flask db migrate
```

Создать базу данных:

```
flask db upgrade
```

Запустить:

```
flask run
```

## Автор
[Мусатова Татьяна](https://github.com/Tatiana314)
