FROM python:3.7.7-slim

WORKDIR web_service

RUN apt-get update && apt-get install -y \
    libpq-dev \
    python-dev \
    vim \
    git

COPY requirements.txt /web_service
RUN pip3 install -r requirements.txt

COPY . /web_service