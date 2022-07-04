FROM python:3.10-alpine

LABEL maintainer="Vyacheslav Kapitonov"
LABEL email="vyach.kapitonov@gmail.com"

RUN apk add --no-cache py3-pip

COPY . /src

WORKDIR /src

RUN  pip3 install pip -U .

WORKDIR /src/src/phone

EXPOSE 8080

ENTRYPOINT ["uvicorn", "server:app", "--port", "8080"]
