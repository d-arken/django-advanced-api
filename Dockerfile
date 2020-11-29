FROM python
LABEL maintainer="darkm dev"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apt-get update
RUN apt-get install postgresql-client -y
RUN apt-get clean

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN useradd -ms /bin/bash eddie
USER eddie

