#!/bin/bash

cd $TESSERACT

./autogen.sh
./configure
make
make install
ldconfig
make training
make training-install
