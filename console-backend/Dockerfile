FROM python:3.10.2-buster

WORKDIR /usr/src/app

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get -y --no-install-recommends install \
        cmake \
        make \
        gcc \
        g++ \
        libssl-dev \
        netcat

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /usr/src/app

COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh