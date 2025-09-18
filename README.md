# pythonCourse
# Предустановка
```pip install pre-commit # Установка pre-commit```

```pre-commit install #  Установка хуков```

```touch .pre-commit-config.yaml # Создание файла .pre-commit-config.yaml```

# Структура хуков в .yaml файле
```repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks # Ссылка на гит хука

    rev: v4.4.0  # Версия или тег репозитория

    hooks:       # Список хуков из этого репозитория

      - id: trailing-whitespace  # Идентификатор хука

        // Дополнительные параметры для хуков:

        name: Remove trailing whitespace  # Человекочитаемое имя

        description: "Removes trailing whitespace from files"  # Описание

        types: [text]  # Типы файлов для обработки

        exclude: '^tests/'  # Исключаемые пути

        args: [--some-arg, value]  # Аргументы для хука

        stages: [commit]  # Этапы

        language: python  # Язык реализации

        files: .\py$      # Регулярное выражение для файлов

        require_serial: true  # Запускать последовательно

      - id: end-of-file-fixer  # Еще один хук из того же репозитория
      #  Можно указать только id, остальное по умолчанию
```
# Примеры настройки хуков через .yaml файл
```repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace # Удаляет пробелы которые мы случайно оставили
      - id: check-yaml

    # Black - форматтер кода
    # Назначение: Автоматическое форматирование Python кода согласно PEP 8.
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
        args: [--line-length=88]

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
        args: [--max-line-length=88, --ignore=E203,W503]

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: ["--profile", "black"]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.3.0
    hooks:
      - id: mypy
        exclude: ^tests/

  - repo: https://github.com/pycqa/bandit
    rev: 1.7.5
    hooks:
      - id: bandit
        args: ["-ll", "-x", "tests"]

  // Локальные хуки (если нужны)
  - repo: local
  hooks:
    - id: pytest-check
      name: pytest check
      entry: python -m pytest -x --tb=short
      language: system
      types: [python]
      stages: [commit]
```
# Black - форматтер кода
## Назначение: Автоматическое форматирование Python кода согласно PEP 8.
```
- repo: https://github.com/psf/black
  rev: 23.3.0
  hooks:
    - id: black
      # Дополнительные параметры:
      args: [--line-length=88, --skip-string-normalization]
      # Исключить тестовые файлы из форматирования:
      exclude: ^tests/

  # Важные аргументы Black

--line-length=88 - максимальная длина строки

--skip-string-normalization - не нормализовать строки

--include - включить конкретные файлы/паттерны

--exclude - исключить файлы/паттерны
```

# Flake8 - линтер
## Назначение: Проверка кода на соответствие стилю и обнаружение ошибок.

```
- repo: https://github.com/pycqa/flake8
  rev: 6.0.0
  hooks:
    - id: flake8
      args: [
        --max-line-length=88,
        --ignore=E203,W503,  # Игнорируемые ошибки
        --max-complexity=10  # Максимальная сложность функций
      ]
      // Обрабатывать только Python файлы:
      types: [python]

  Основные коды ошибок Flake8:

    E*** - ошибки из pycodestyle (PEP 8)

    W*** - предупреждения из pycodestyle

    F*** - ошибки из PyFlakes (логические ошибки)

    C9** - сложность кода из mccabe
```

# isort - сортировщик импортов
## Назначение: Автоматическая сортировка и форматирование импортов.

```
- repo: https://github.com/pycqa/isort
  rev: 5.12.0
  hooks:
    - id: isort
      name: isort (python)
      args: [
        --profile=black,        # Совместимость с Black
        --line-length=88,
        --multi-line=3,         # Стиль многострочных импортов
        --trailing-comma        # Добавлять запятую после последнего импорта
      ]
    # Профили isort:

    black - совместимость с Black

    django - для Django проектов

    pycharm - стиль PyCharm

    google - стиль Google
```
# Yamllint
## yamllint — это линтер для YAML файлов, который проверяет
 - __Синтаксическую корректность (валидность YAML)__
 - __Стилистические правила (отступы, форматирование)__
 - __Лучшие практики (конвенции написания)__
