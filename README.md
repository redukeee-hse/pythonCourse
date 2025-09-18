# pythonCourse
Установка pre-commit:
  pip install pre-commit
  
Установка хуков:
  pre-commit install

Создайте файл .pre-commit-config.yaml:
  touch .pre-commit-config.yaml

Добавьте базовую конфигурацию в .pre-commit-config.yaml:
  repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: check-yaml // Проверка на валидность всех .yaml файлов 
Установите pre-commit хуки:
  pre-commit install



