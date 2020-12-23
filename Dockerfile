FROM python:3.8.5-alpine3.12

## Install OpenSSL
RUN apk upgrade --update-cache --available && \
    apk add openssl && \
    rm -rf /var/cache/apk/*

## Install Application
WORKDIR /notifikator
COPY ./setup.cfg /notifikator
COPY ./setup.py /notifikator
COPY ./app /notifikator/app
COPY ./test /notifikator/test
COPY ./CHANGES.rst ./
COPY ./LICENSE.rst ./
COPY ./README.md ./
COPY ./boot.sh ./boot.sh
RUN pip install -e .
RUN chmod 775 ./boot.sh

ENTRYPOINT [ "/notifikator/boot.sh" ]
