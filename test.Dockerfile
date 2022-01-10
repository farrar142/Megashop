FROM python:3.10

LABEL Farrar142 "gksdjf1690@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY wait.sh .
COPY . .

RUN pip3 install -r requirements/dev.txt \
    && apt-get update \
    && apt-get install netcat-openbsd -y

ENTRYPOINT python3 dev.py migrate && python3 dev.py runserver 0.0.0.0:8000
EXPOSE 8000