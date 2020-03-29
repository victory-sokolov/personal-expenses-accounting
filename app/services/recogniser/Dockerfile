FROM python:3.7.7-slim

RUN apt update && apt install -y \
    tesseract-ocr \
    cmake \
    libgtk2.0-dev \
    pkg-config \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    imagemagick \
    vim \
    git \
    wget

WORKDIR /recogniser
COPY requirements.txt /recogniser
RUN pip3 install -r requirements.txt

COPY . /recogniser