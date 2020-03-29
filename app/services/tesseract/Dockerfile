FROM ubuntu:19.10

ENV DEBIAN_FRONTEND=noninteractive
ENV TESSERACT=/usr/share/tesseract

WORKDIR /tesseract

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    python3.7 \
    python3-pip \
    cmake \
    autoconf \
    automake \
    libtool \
    pkg-config \
    libpng-dev \
    tesseract-ocr \
    libtesseract-dev \
    libpango1.0-dev \
    libicu-dev \
    libcairo2-dev \
    libjpeg8-dev \
    zlib1g-dev \
    libtiff5-dev \
    wget \
    git \
    g++ \
    vim

RUN git clone https://github.com/tesseract-ocr/tesseract $TESSERACT

COPY requirements.txt /tesseract
RUN pip3 install -r requirements.txt

COPY scripts/ /tesseract/scripts

RUN chmod +x scripts/*
RUN ./scripts/compile_tesseract.sh
RUN ./scripts/langdata_lstm.sh

COPY . /tesseract/
ENV TESSDATA_PREFIX=/usr/share/tesseract/tessdata