#!/bin/bash
if [ ! -f .env ]; then
  SECRET=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 16)
  echo "SECRET_KEY=$SECRET" > .env
fi

python3 manage.py makemigrations home --no-input

python3 manage.py migrate 

python3 manage.py createsuperuser --no-input

python3 manage.py collectstatic --noinput


