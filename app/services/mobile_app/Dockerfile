FROM node:latest

WORKDIR /app
COPY . /app/

RUN apt-get update && apt-get install -y \
    software-properties-common \
    apt-transport-https \
    ca-certificates \
    python \
    python-dev \
    curl \
    wget \
    android-tools-adb \
    android-sdk \
    openjdk-8-jdk \
    yarn \
    git

# Define  JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64


# ——————————
# Installs Android SDK
# ——————————
ARG SDK_VERSION=sdk-tools-linux-4333796.zip
ARG ANDROID_BUILD_VERSION=29
ARG ANDROID_TOOLS_VERSION=29.0.2
ARG BUCK_VERSION=2019.10.17.01
ARG NDK_VERSION=20.0.5594570
ARG NODE_VERSION=12.x
ARG WATCHMAN_VERSION=4.9.0

# set default environment variables
ENV ADB_INSTALL_TIMEOUT=10
ENV ANDROID_HOME=/opt/android
ENV ANDROID_SDK_HOME=${ANDROID_HOME}
ENV ANDROID_NDK=${ANDROID_HOME}/ndk/$NDK_VERSION

ENV PATH=${ANDROID_NDK}:${ANDROID_HOME}/emulator:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools:/opt/buck/bin/:${PATH}

# download and install buck using debian package
RUN curl -sS -L https://github.com/facebook/buck/releases/download/v${BUCK_VERSION}/buck.${BUCK_VERSION}_all.deb -o /tmp/buck.deb \
    && dpkg -i /tmp/buck.deb \
    && rm /tmp/buck.deb

RUN curl -sS https://dl.google.com/android/repository/${SDK_VERSION} -o /tmp/sdk.zip \
    && mkdir ${ANDROID_HOME} \
    && unzip -q -d ${ANDROID_HOME} /tmp/sdk.zip \
    && rm /tmp/sdk.zip \
    && yes | sdkmanager --licenses \
    && yes | sdkmanager \
        "platform-tools" \
        "emulator" \
        "platforms;android-28" \
        "platforms;android-$ANDROID_BUILD_VERSION" \
        "build-tools;28.0.3" \
        "build-tools;$ANDROID_TOOLS_VERSION" \
        "add-ons;addon-google_apis-google-23" \
        "system-images;android-19;google_apis;armeabi-v7a" \
        "extras;android;m2repository" \
        "ndk;$NDK_VERSION" \
    && rm -rf /opt/android/.android
RUN "android update sdk --no-ui"

# GRADLE
RUN curl -sL -o gradle.zip https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip &&\
    mkdir /opt/gradle && unzip -d /opt/gradle gradle.zip && rm gradle.zip

# Install Watchman
RUN apt-get update \
    && apt-get install -y pkg-config libssl-dev autoconf automake libtool \
    && cd /tmp \
    && git clone https://github.com/facebook/watchman.git \
    && cd watchman \
    && git checkout v${WATCHMAN_VERSION} \
    && ./autogen.sh \
    && ./configure \
    && make \
    && make install \
    && cd $HOME \
    && rm -rf /tmp/watchman

# NPM Installation
RUN npm install react-native-cli -g
RUN npm install --silent

#CMD adb connect $ADB_IP && yarn run android