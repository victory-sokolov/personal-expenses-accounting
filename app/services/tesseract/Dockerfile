FROM tesseractshadow/tesseract4cmp

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /tesseract

COPY . /tesseract/

RUN apt-get update && apt-get install -y \
    vim \
    git \
    wget


