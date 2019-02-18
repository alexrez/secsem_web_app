Веб-приложение (Python3, aihttp, postgresql)

Зависимости перечислены в файле requirements.txt

Для корректного запуска приложения и его работы необходимо установить следующие библиотеки:
$ pip install aiohttp
$ pip install asyncpgsa
$ pip install pyyaml
$ pip install aiohttp_jinja2

Установить, если отсутствует, postgresql, настроить права доступа:
$ sudo -u postgres psql
psql=# alter user <username> with encrypted password '<password>';

Создать БД:
$ createdb db_users

И инициализировать ее:
$ psql -d db_users -f init-db.sql

Исполнить файл запуска:
$ python main.py


http://0.0.0.0:8080
