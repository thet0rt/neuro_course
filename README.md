# Opening hours (hw-1)
Приложение на fastapi с одним эндпоинтом, который принимает время работы в формате json и возвращает в текстовом
формате, удобном для чтения.

## Содержание
- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Тестирование](#тестирование)
- [Deploy и CI/CD](#deploy-и-ci/cd)
- [Contributing](#contributing)
- [To do](#to-do)
- [Команда проекта](#команда-проекта)

## Технологии
- [GatsbyJS](https://www.gatsbyjs.com/)
- [TypeScript](https://www.typescriptlang.org/)
- ...

## Использование

Запускаем контейнер
```
docker-compose up --build
```
Заходим в swagger http://0.0.0.0:8005/docs
Делаем post-запрос /opening_hours

## Разработка

### Требования
Для установки и запуска проекта, необходим [Python 3.10](https://www.python.org/downloads/release/python-3100/) v8+.

### Установка зависимостей
Для установки зависимостей, выполните команду:
```
pip install -r requirements.txt
```

### Запуск Development сервера
Чтобы запустить сервер для разработки, выполните команду:
```
uvicorn main:app --reload
```

### Создание билда
Чтобы выполнить production сборку, выполните команду: 
```
docker-compose up --build
```

## Тестирование
Проект покрыт тестами pytest. Для их запуска выполните команду:
```
make
```