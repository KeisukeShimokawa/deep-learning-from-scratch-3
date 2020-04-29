FROM python:3
USER root

RUN apt-get update \
    && apt-get -y install locales vim git graphviz \
    && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install numpy matplotlib pylint black

WORKDIR /home/app