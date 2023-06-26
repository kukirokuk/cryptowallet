FROM python:3.8-slim-bookworm

RUN apt-get update -y && apt install -y libgmp-dev gcc

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /cryptowallet

RUN mkdir backup

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

RUN python manage.py migrate

RUN python manage.py dbrestore --noinput 