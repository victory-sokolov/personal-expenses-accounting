FROM ubuntu:18.04
LABEL maintainer="Viktor Sokolov"

RUN apt-get update && apt-get install -y \
  software-properties-common \
  python3-pip \
  build-essential \
  vim \
  wget \
  curl \
  git \
  gcc \
  make \
  --no-install-recommends

RUN mkdir /home/app
WORKDIR /home/app/

#COPY requirements.txt /home/app
RUN pip3 install virtualenv
#RUN pip3 install -r /home/app/requirements.txt

COPY start.sh /home/app


ENV PYTHONIOENCODING=UTF-8 \
  PYTHONDONTWRITEBYCODE=1

