# 📝 FastAPI + SQLAlchemy + PostgreSQL — CRUD API для пользователей и заметок

## 📌 Описание

Проект реализует REST API на базе FastAPI, с подключением к базе данных PostgreSQL через SQLAlchemy ORM. Реализованы сущности **User** и **Note**, связанные отношением *один ко многим* (один пользователь может иметь несколько заметок).

---

## 🚀 Технологии

- Python 3.10+
- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Pydantic
- Uvicorn

---

### ⚙️ Установка и запуск

## 1. Клонируйте репозиторий

```bash
git clone https://github.com/yourusername/fastapi-notes-crud.git
cd fastapi-notes-crud
```
## 2. Создайте и активируйте виртуальное окружение
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```
## 3. Установите зависимости
```bash
pip install -r requirements.txt
```
## 4. Проверьте подключение к базе
Подключение по умолчанию настроено на:
```python
postgresql://postgres:password@<ip_ubuntu>/<db_name>
```
Если база ещё не создана, создайте её вручную:
```sql
CREATE DATABASE mydb;
```
При необходимости отредактируйте строку подключения в файле database.py.

## 5. Запуск сервера
```bash
uvicorn main:app --reload
```
### 🧪 Документация API
После запуска перейдите на:

http://localhost:8000/docs — Swagger UI

http://localhost:8000/redoc — ReDoc

### 📚 Основные эндпоинты
Пользователи:
POST /users/ — создать пользователя

GET /users/ — получить список пользователей

GET /users/{user_id} — получить пользователя по ID

Заметки:
POST /notes/ — создать заметку (указать user_id)

GET /notes/ — получить все заметки

GET /notes/{note_id} — получить заметку по ID

GET /users/{user_id}/notes — получить заметки конкретного пользователя

PUT /notes/{note_id} — обновить заметку

DELETE /notes/{note_id} — удалить заметку

### 📂 Структура проекта
.
├── main.py         # Точка входа FastAPI-приложения
├── models.py       # SQLAlchemy ORM-модели
├── schemas.py      # Pydantic-схемы (ввод/вывод)
├── crud.py         # CRUD-операции
├── database.py     # Подключение и конфигурация БД
├── requirements.txt
└── README.md

### ✅ Возможности
Полноценный CRUD по пользователям и заметкам

Работа с PostgreSQL через SQLAlchemy

Чистая архитектура с разделением моделей, схем и логики

Поддержка OpenAPI-документации

Готово для расширения (авторизация, миграции, асинхронность и т.д.)