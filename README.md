# FinalWork_FN

# ChitaiGorod

## Описание
 Это набор автоматизированных тестов для веб-приложения, использующих библиотеку selenium и allure для генерации отчётов. Тесты проверяют основные функциональности приложения: 
 *авторизация, 
 *выполнение действий на страницах.



## Структура проекта

 - **api_chitaigorod.py**: Содержит класс PageObject для выполнения поиска товаров.
 - **ui_chitaigorod.py**: Содержит класс PageObject для разных страниц приложений.
 - **test_api_chitaigorod.py, test_api_chitaigorod.py**: Содержит тестовые сценарии.
 - **config.py**: Содержит настройку окружения,тестовые данные.
 - **requirements.txt**: Список зависимостей проекта.
 - **readme.md**: Документация проекта.

## Запуск тестов
  1 Установить зависимости:
  ```
   pip install -r requirements.txt
  ```
  2 В файл config.py вставить API_URL, UI_URL, MY_TOKEN, MY_USER_AGENT
  ```
  3 Запустить все тесты и укажиу путь к каталогу результатов тестирования:
  ```
  pytest --alluredir allure-result
  ```
  4 Ввести команду для генерации отчета о тестах:
  ```
  C:\Users\<Пользователь>\scoop\apps\allure\current\bin\allure serve allure-result
  ``` allure-result
   - Заменить `<Пользователь>` на имя твоего пользователя.
  ```
  5 Запустить API тесты
  ```
  pytest test_api_chitaigorod.py
  ```
  5 Запустить UI тесты
  ```
  pytest test_ui_chitaigorod.py
  ```
