FROM python:latest

LABEL Farrar142 "gksdjf1690@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY wait.sh .
COPY requirements.txt .
COPY ../../. .

RUN pip3 install -r requirements.txt \
    && apt-get update \
    && apt-get upgrade \
    && apt-get install netcat-openbsd -y

ENTRYPOINT chmod +x wait.sh \
    && ./wait.sh
EXPOSE 8000
#