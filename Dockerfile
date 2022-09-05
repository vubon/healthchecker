FROM python:3.9.10-slim-buster

# Skip the configuration part
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get -y install libpq-dev gcc

# MAINTAINER vubon.roy@gmail.com

# Project Files and Settings
ARG PROJECT=healthchecker
ARG PROJECT_DIR=/var/www/${PROJECT}
RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR
ADD requirements.txt $PROJECT_DIR
RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt
COPY . $PROJECT_DIR

RUN ["chmod", "+x", "/var/www/healthchecker/start.sh"]

# Server
EXPOSE 8000

# RUN Server
CMD ["/var/www/healthchecker/start.sh"]
