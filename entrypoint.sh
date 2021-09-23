#!/bin/bash

python manage.py makemigrations

python manage.py migrate

#  cat /proc/cpuinfo | grep 'core id' | wc -l  (returns number of CPU cores)
exec gunicorn -w $(( 2 * `cat /proc/cpuinfo | grep 'core id' | wc -l` + 1 )) -t 60 src.config.wsgi:application -b 0.0.0.0:8000 --reload
