# 🧪 test_booking

Автоматизированные тесты для API [Restful Booker](https://restful-booker.herokuapp.com/) на Python с использованием `pytest` и `requests`.

## 📁 Структура проекта

```text
restful-booker/
│
├── test_booking.py         # Основной набор тестов
├── conftest.py             # Фикстуры: авторизация, данные, сессии
├── requirements.txt        # Зависимости проекта
├── README.md               # Описание проекта
└── ...
```

## 🚀 Быстрый старт

1. Клонируй репозиторий:

```bash
git clone https://github.com/RAXAS/test_booking.git
cd test_booking
```

2. Создай и активируй виртуальное окружение:

```bash
python -m venv .venv
source .venv/bin/activate     # для Linux/Mac
.venv\Scripts\activate      # для Windows
```

3. Установи зависимости:

```bash
pip install -r requirements.txt
```

4. Запусти тесты:

```bash
pytest -v
```

## ⚙️ Переменные

Проверь значения в `conftest.py`:

- `BASE_URL`: адрес API (по умолчанию `https://restful-booker.herokuapp.com`)
- `AUTH_JSON`: логин/пароль для получения токена
- `HEADERS`: базовые заголовки для запросов

## 📌 Основные возможности

- Тестирование создания, получения и удаления бронирований
- Проверка авторизации и работы без неё
- Валидация JSON-ответов
- Использование `pytest fixtures` для переиспользуемости

## 🧰 Используемые технологии

- `pytest` — фреймворк для написания тестов
- `requests` — HTTP-клиент
- `Python 3.10+`

## 📄 Лицензия

Проект открыт для обучения и тестирования. Использование — по договорённости.
