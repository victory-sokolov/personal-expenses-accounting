FROM node:latest

RUN apt-get update && \
    apt-get install android-tools-adb

WORKDIR /app
COPY package.jso yarn.lock app.json ./

CMD adb connect $ADB_IP && yarn run android