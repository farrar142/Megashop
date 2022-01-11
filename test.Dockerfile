FROM python:3.10

LABEL Farrar142 "gksdjf1690@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY wait.sh .
COPY . .

RUN pip3 install -r requirements/dev.txt \
    && apt-get update

ENTRYPOINT python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000
EXPOSE 8000