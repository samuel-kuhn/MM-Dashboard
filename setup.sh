#!/bin/bash
python3 /app/manage.py makemigrations --no-input

python3 /app/manage.py migrate 

python3 /app/manage.py createsuperuser --no-input

python3 /app/manage.py collectstatic --noinput


