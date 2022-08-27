# VTiSS - тестовое задание

Адрес проекта: http://158.160.7.120

Login: admin@admin.ru
Password: 1234

## Описание проекта 


## Запуск проекта в dev-режиме

Установить и активировать виртуальное окружение:
```
python -m venv venv
source /venv/bin/activated
```

Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:
```
python manage.py makemigrations

python manage.py migrate
```

Создать суперпользователя:
```
python manage.py createsuperuser
```

В папке с файлом manage.py выполнить команду:
```
python manage.py runserver
```

## Запуск проекта на сервере с помощью Docker

Установить docker, docker-compose на сервере с ОС Linux:
```
sudo apt update && sudo apt upgrade -y && sudo apt install curl -y
```
```
sudo curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh && sudo rm get-docker.sh
```
```
sudo curl -L "https://github.com/docker/compose/releases/download/v2.9.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
```
sudo chmod +x /usr/local/bin/docker-compose
```

Создать директорию infra:

```
mkdir infra
```
Перенести файлы docker-compose.yml и nginx.conf 
из скачанного проекта на сервер в директорию infra.

Находясь в папке с файлами выполнить:
```
scp docker-compose.yml ваш_user_name@server_ip:/home/ваш_user_name/infra
```
```
scp nginx.conf ваш_user_name@<server_ip>:/home/ваш_user_name/infra
```

Перейти в каталог:
```
cd infra/
```

Добавить файл .env в котором хранится SECRET_KEY и настройки БД:
```bash
echo "SECRET_KEY=YourSecretKey 
DB_ENGINE=django.db.backends.postgresql 
DB_NAME=postgres 
POSTGRES_USER=postgres 
POSTGRES_PASSWORD=1234 
DB_HOST=db 
DB_PORT=5432" > .env
```
Пример заполнения файла .env:
```
SECRET_KEY=mysup3r4w3s0me53cr3tk3y
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql 
DB_NAME=postgres # имя базы данных 
POSTGRES_USER=postgres # логин для подключения к базе данных 
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой) 
DB_HOST=db # название сервиса (контейнера) 
DB_PORT=5432 # порт для подключения к БД
```
В директории infra выполнить команду:
```
sudo docker-compose up -d
```

Выполнить миграции:
```
sudo docker-compose exec web python manage.py makemigrations
```
```
sudo docker-compose exec web python manage.py migrate --noinput
``` 
Собрать статику:
```
sudo docker-compose exec web python manage.py collectstatic --no-input
```
Создать суперпользователя:
```
sudo docker-compose exec backend python manage.py createsuperuser
```