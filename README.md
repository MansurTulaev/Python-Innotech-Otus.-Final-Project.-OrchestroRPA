# OpenRPA Orchestrator

Простой оркестратор RPA на Django с JWT аутентификацией, REST API и поддержкой ботов и задач.

## Возможности

- Управление пользователями, ботами и задачами через REST API
- JWT аутентификация
- Swagger-документация
- Тесты с покрытием pytest и coverage
- CI/CD с GitHub Actions

## Установка

1. Клонировать репозиторий  

git clone <url>
cd openrpa

2. Создать и активировать виртуальное окружение

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Установить зависимости
pip install -r requirements.txt

4. Выполнить миграции
python manage.py migrate

5. Создать суперпользователя
python manage.py createsuperuser

6. Запустить сервер
python manage.py runserver
