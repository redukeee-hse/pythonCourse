# Что такое Poetry?
Poetry — это современный инструмент для управления зависимостями и упаковки в Python. Он объединяет функциональность pip, virtualenv, setuptools, twine и pipenv в одном инструменте.

Ключевые возможности:
Управление зависимостями с разрешением версий

Автоматическое создание виртуальных окружений

Упаковка и публикация пакетов

Поддержка pyproject.toml (PEP 518)


# Установка Poetry
Официальный способ установки:
***Linux/macOS/WSL***
```curl -sSL https://install.python-poetry.org | python3 -```

***Windows (PowerShell)***

```pip install --user poetry```

# Интерактивная инициализация
```poetry init

# Package name [my-project]: 
# Version [0.1.0]: 
# Description []: My awesome project
# Author [Your Name <email@example.com>]: 
# License []: MIT
# Compatible Python versions [^3.8]:
```

### Package name [my-project]:
Что это: Имя вашего пакета/проекта

Что вписать:
```
Используйте snake_case (нижний регистр, подчеркивания) или kebab-case (дефисы)

Должно быть уникальным на PyPI (если планируете публикацию)

Отражает суть проекта
```
### Version [0.1.0]:
Что это: Версия вашего пакета

Что вписать:
```
Следуйте Semantic Versioning (MAJOR.MINOR.PATCH)

0.1.0 - хорошая начальная версия для нового проекта

1.0.0 - первая стабильная версия
```
Формат:
```
MAJOR - обратно несовместимые изменения

MINOR - новая функциональность с обратной совместимостью

PATCH - исправления ошибок с обратной совместимостью
```
### Description []:
Что это: Краткое описание вашего проекта

Что вписать:
```
1-2 предложения о назначении проекта

Ясно и понятно описывает функциональность

Можно использовать на PyPI и в документации
```
### Author [Your Name email@example.com]:
Что это: Информация об авторе/авторах

Что вписать:
```
Формат: Имя Фамилия <email@example.com>

Можно указать нескольких авторов через запятую

Email используется для контактов по поводу пакета
```
### License []:
Что это: Лицензия вашего проекта

Что вписать:
```
Укажите SPDX идентификатор лицензии

Для открытого ПО: MIT, Apache-2.0, GPL-3.0

Для проприетарного: Proprietary
```
### Compatible Python versions [^3.8]:
Что это: Совместимые версии Python

Что вписать:

Укажите диапазон поддерживаемых версий Python

Используйте спецификаторы версий Poetry

Синтаксис:
```
^3.8 - 3.8 или выше, но ниже 4.0 (>=3.8,<4.0)

>=3.8 - 3.8 или выше

>=3.8,<3.12 - от 3.8 до 3.11 включительно

3.8 || 3.9 - 3.8 или 3.9
```

# Структура проекта Poetry
После создания проекта вы получите следующую структуру:
```
text
my-project/
├── pyproject.toml          # Основной файл конфигурации
├── README.md               # Документация проекта
├── poetry.lock             # Файл блокировки версий
├── src/                    # Исходный код (опционально)
│   └── my_project/
│       ├── __init__.py
│       └── example.py
└── tests/                  # Тесты
    ├── __init__.py
    └── test_my_project.py
 ```
# Файл pyproject.toml:
```
[tool.poetry]
name = "my-project"
version = "0.1.0"
description = "My awesome project"
authors = ["Your Name <email@example.com>"]
license = "MIT"
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.8"

[tool.poetry.dev-dependencies]
pytest = "^7.0"
black = "^22.0"
flake8 = "^5.0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```
# Управление зависимостями
### Основные секции зависимостей
```
[tool.poetry.dependencies]
python = "^3.8"  # Обязательные зависимости
requests = "^2.28.0"
django = "^4.0"

[tool.poetry.dev-dependencies]  # Зависимости для разработки
pytest = "^7.0"
black = "^22.0"
flake8 = "^5.0"

[tool.poetry.group.dev.dependencies]  # Группы зависимостей (Poetry 1.2+)
pytest = "^7.0"
pytest-cov = "^3.0"

[tool.poetry.group.docs.dependencies]
sphinx = "^5.0"
```
## Спецификаторы версий:
```
^ Совместимые версии	^2.1.0 → >=2.1.0, <3.0.0
~	Приблизительные версии	~2.1.0 → >=2.1.0, <2.2.0
*	Любая версия
>=	Больше или равно	>=2.0.0
<=	Меньше или равно	<=2.5.0
==	Точная версия	==2.1.0
```
# Виртуальное окружение
## Автоматическое управление:
### Создать виртуальное окружение (автоматически)
```
poetry install
```
### Показать информацию о виртуальном окружении
```
poetry env info
```
### Список виртуальных окружений
```
poetry env list
```
### Активировать виртуальное окружение
```
poetry shell
```
### Запуск команды в виртуальном окружении без активации
```
poetry run python script.py
```
### Деактивация (если активировали через poetry shell)
```
exit
```
## Ручное управление:
### Использовать конкретную версию Python
```
poetry env use /usr/bin/python3.9
```
### Удалить виртуальное окружение
```
poetry env remove python3.9
```
# Установка и удаление пакетов

## Добавление зависимостей:
### Добавить production зависимость
```
poetry add requests
```
### Добавить dev зависимость
```
poetry add --dev pytest
```
### Или (новый синтаксис)
```
poetry add pytest --group dev
```
### Добавить с конкретной версией
```
poetry add "django>=4.0,<5.0"
```
### Добавить несколько пакетов
```
poetry add requests pandas numpy
```
### Добавить из git репозитория
```
poetry add git+https://github.com/username/repo.git
```
### Добавить из локального пути
```
poetry add ./local-package
```

## Удаление зависимостей:
### Удалить зависимость
```
poetry remove requests
```
### Удалить dev зависимость
```
poetry remove pytest --group dev
```
## Обновление зависимостей:
### Обновить все зависимости
```
poetry update
```
### Обновить конкретный пакет
```
poetry update requests
```
### Показать устаревшие пакеты
```
poetry show --outdated
```
# Команды Poetry
## Основные команды:
### Инициализация проекта
```
poetry init
```
### Установка зависимостей
```
poetry install
```
### Добавление пакетов
```
poetry add <package>
```
### Удаление пакетов
```
poetry remove <package>
```
### Обновление пакетов
```
poetry update
```
### Запуск в виртуальном окружении
```
poetry run <command>
```
### Активация shell
```
poetry shell
```
### Показать зависимости
```
poetry show
poetry show --tree
```
### Экспорт requirements.txt
```
poetry export -f requirements.txt --output requirements.txt
```
## Команды для разработки:
### Запуск тестов
```
poetry run pytest
```
### Форматирование кода
```
poetry run black .
```
### Линтинг
```
poetry run flake8
```
### Проверка типов
```
poetry run mypy .
```

### Показать детальную информацию о зависимостях
```
poetry show --tree
```
### Проверить конфигурацию
```
poetry check
```
### Очистить кэш
```
poetry cache clear --all .
```
### Показать информацию о окружении
```
poetry env info
```
