FROM python:alpine

RUN apk add --no-cache wget unzip postgresql-client postgresql-dev openssl gcc python3-dev musl-dev && pip3 install psycopg2

RUN pip install --no-cache-dir psycopg2

RUN mkdir /fooddata && \
  cd /fooddata && \
  wget --no-check-certificate https://www.canada.ca/content/dam/hc-sc/migration/hc-sc/fn-an/alt_formats/zip/nutrition/fiche-nutri-data/cnf-fcen-csv.zip && \
  unzip cnf-fcen-csv.zip

ENV DOCKERIZE_VERSION v0.5.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

COPY run.sh /run.sh
COPY tables.sql /data/tables.sql
COPY loaddata.py /scripts/loaddata.py

ENTRYPOINT /run.sh
