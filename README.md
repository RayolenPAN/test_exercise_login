# test_exercise_login
Тестовое задание: AQA Python
Автоматизация тестирования авторизации на сайте [SauceDemo](https://www.saucedemo.com/).
## Технологии

- **Python 3.10**
- **Playwright** для автоматизации браузера
- **Pytest** как фреймворк для тестирования
- **Allure** для отчетов
- **Docker** для контейнеризации
## Структура проекта
test_exercise_login
- allure-results # отчеты по тестированию
- pages # Page Object классы
- tests # Тестовые сценарии
- requirements.txt # Зависимости Python
- Dockerfile # Конфигурация Docker
- README.md # Документация
- pytest.ini # Конфигурация Pytest
## Запуск проекта
1. Клонирование репозитория
2. Если установлен python, то необходимо установить зависимости (через терминал среды разработки):  
   pip install -r requirements.txt  
   установить браузер для Playwright  
   playwright install chromium  
3. Запуск тестов с отчетами allure
   pytest tests/ --alluredir=allure-results -v
