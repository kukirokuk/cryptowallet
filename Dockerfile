FROM python:3.8-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /cryptowallet

RUN mkdir backup

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .
