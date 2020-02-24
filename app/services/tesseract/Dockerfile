FROM tesseractshadow/tesseract4cmp

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR = /workspace

RUN apt-get update && apt-get install -y \
    vim

COPY start.sh
# copy fonts directory
COPY ../../../fonts/*.ttf ~/.fonts

CMD ['~/start.sh']