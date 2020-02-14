#!/bin/sh

# installation:
# https://github.com/tesseract-ocr/tesseract/wiki
# https://tesseract-ocr.github.io/tessdoc/Compiling-%E2%80%93-GitInstallation.html

sudo apt-get install build-essential
sudo apt-get install tesseract-ocr libtesseract-dev libpango1.0-dev -y

# Languages
sudo apt-get install tesseract-ocr-lav -y
sudo apt-get install imagemagick make -y

# Libs
sudo apt-get install libicu-dev libpango1.0-dev libcairo2-dev
cd /usr/share/tesseract-ocr
sudo git clone https://github.com/tesseract-ocr/tesseract
# download manually files for your language
# sudo git clone https://github.com/tesseract-ocr/langdata_lstm

cd tesseract

sudo ./autogen.sh
sudo ./configure
sudo make
sudo make install
sudo ldconfig
sudo make training
sudo make training-install
