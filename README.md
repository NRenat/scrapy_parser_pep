# Проект парсинга pep
Парсер собирает данные pep c https://docs.python.org/3/.

Установка зависимостей:

`pip install -r pip install -r requirements.txt`

Запуск парсера:

`scrapy crawl pep`

На выходе получаем два .csv файла: 
* Заголовок, номер, статус всех собранных pep
* Подсчитанное количество статусов pep