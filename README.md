# Quiz API using DRF and Docker

[![Build Status](https://travis-ci.org/ajithpmohan/quiz-api.svg?branch=master)](https://travis-ci.org/ajithpmohan/quiz-api)

## System Requirements

You need **Docker Engine** and **Docker Compose**. Install it from [Docker Website](https://docs.docker.com/)

## Usage

Download the repository:

    git clone git@github.com:ajithpmohan/quiz-api.git

## Python Environment Setup

Try [python-decouple](https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html) library for handling environment variables.

## Permission Required

Before building the services update the file permission of `web/entrypoint.sh`

    chmod +x web/entrypoint.sh

## Build the Services

    docker-compose build

## Starting App

    docker-compose up

## Swagger
Access it through [http://0.0.0.0:9001/swagger/](http://0.0.0.0:9001/swagger/)

## Code Styling

Before code pushing, run [flake8](https://simpleisbetterthancomplex.com/packages/2016/08/05/flake8.html) for code styling and [isort](https://simpleisbetterthancomplex.com/packages/2016/10/08/isort.html) for organizing the python imports.

    docker-compose exec web flake8
    docker-compose exec web isort -rc .
