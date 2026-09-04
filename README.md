# CRMLite

Основные возможности:
- регистрация пользователей
- JWT-аутентификация
- создание компании
- добавление пользователей в компанию
- управление складами компании
- разграничение доступа между владельцем компании и сотрудниками
- Swagger-документация API

## Стек

- Python
- Django
- Django REST Framework
- SimpleJWT
- drf-spectacular
- SQLite

## Установка

### 1. Клонировать репозиторий

```bash
git clone https://github.com/meixcore/CRMlite.git
```

### 2. Создать виртуальное окружение

```bash
python -m venv .venv
```

### 2. Создать виртуальное окружение

```
.venv\Scripts\activate
```

### 3. Установить зависимости

```
poetry install
```

### 4. Создать окружение

```
.env
```
```
DJANGO_SECRET_KEY=
DEBUG=True
ALLOWED_HOSTS=
DB_PASS=
DB_NAME=
DB_USER=
DB_HOST=
DB_PORT=
```

### 5. Выполнить миграции

```
python manage.py makemigrations
python manage.py migrate
```
