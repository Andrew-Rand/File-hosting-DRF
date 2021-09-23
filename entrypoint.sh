#!/bin/bash

python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic --no-input

exec gunicorn src.config.wsgi:application -b 0.0.0.0:8000 --reload