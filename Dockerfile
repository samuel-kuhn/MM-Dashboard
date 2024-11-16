FROM python:3.12-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_PASSWORD=password
ENV DJANGO_SUPERUSER_EMAIL=admin@example.net
ENV DISPLAY_SERVER_IP=my-server-url
ENV API_SERVER_IP=host.docker.internal
ENV API_SERVER_PORT=5000

WORKDIR /app

COPY requirements.txt .
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY ./entrypoint.sh /

EXPOSE 8000
# gunicorn
CMD ["/bin/bash", "/entrypoint.sh"]
