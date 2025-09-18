# pythonCourse
# Предустановка
pip install pre-commit - Установка pre-commit

pre-commit install -  Установка хуков

touch .pre-commit-config.yaml - Создание файла .pre-commit-config.yaml

Добавьте базовую конфигурацию в .pre-commit-config.yaml:
  repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: check-yaml // Проверка на валидность всех .yaml файлов

# Настройка хуков через .yaml файл
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml

  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.3.0
    hooks:
      - id: mypy
