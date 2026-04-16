# SQLAlchemy + Alembic Students Database

## Описание
Проект моделирует базу данных студентов и оценок с использованием SQLAlchemy и Alembic.

---

## Модель данных

- Фамилия
- Имя
- Факультет
- Дисциплина
- Оценка

---

## Технологии

- Python
- SQLAlchemy
- Alembic
- SQLite

---

## Запуск

```bash
pip install -r requirements.txt
alembic init alembic
alembic revision --autogenerate -m "init"
alembic upgrade head
python app/main.py