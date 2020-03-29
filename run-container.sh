#!/bin/bash

tesseract() {
        docker run --rm -it -v \
                `pwd`/app/base/ProcessManager.py:/tesseract/base/ProcessManager.py \
                personal-expenses-accounting_tesseract /bin/bash
}


recogniser() {
        docker run --rm -it -v \
                `pwd`/app/base/ProcessManager.py:/recogniser/base/ProcessManager.py \
                personal-expenses-accounting_recogniser /bin/bash
}

"$@"