FROM python:latest

WORKDIR /app

COPY requirements.txt ./

RUN pip install -U -r requirements.txt