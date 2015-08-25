FROM ubuntu:14.04

MAINTAINER John Beieler <jbeieler@caerusassociates.com>

RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main
universe" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y build-essential python-setuptools \
python-dev wget unzip

RUN easy_install pip

ADD . /src

RUN cd /src; pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "/src/app.py"]
