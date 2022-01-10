FROM python:3.10

LABEL Farrar142 "gksdjf1690@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY . .

RUN pip3 install -r requirements/prod.txt
RUN python3 prod.py test