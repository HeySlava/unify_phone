# Test web-app to use with Pluralsight courses and Docker Deep Dive book
# Linux x64
FROM python:3.10-alpine

LABEL maintainer="vyackapitonov"

# Install Node and NPM
RUN apk add py3-pip

# Copy app to /src
# unify-phone-from-json
COPY . /src

WORKDIR /src

# Install dependencies
RUN  pip3 install pip -U .

WORKDIR /src/src/phone

EXPOSE 8080

ENTRYPOINT ["uvicorn", "server:app", "--port", "8080"]
