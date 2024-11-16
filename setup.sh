#!/bin/bash
SECRET=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 16)
echo "SECRET_KEY=$SECRET" > .env

python3 /app/manage.py makemigrations --no-input

python3 /app/manage.py migrate 

python3 /app/manage.py createsuperuser --no-input

python3 /app/manage.py collectstatic --noinput


