# Quiz API using DRF and Docker

## System Requirements

You need **Docker Engine** and **Docker Compose**. Install it from [Docker Website](https://docs.docker.com/)

## Usage

Download the repository:

    git clone https://github.com/ajithpmohan/quiz-api.git

## Python Environment Setup

Copy **.env.dev.sample** to **.env.dev**

    cp .env.dev.sample .env.dev

Try [python-decouple](https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html) library for handling environment variables.

## Build the Services

    docker-compose build

## Starting App

    docker-compose up

Access it through [http://0.0.0.0:8000](http://0.0.0.0:8000)

## Code Styling

Before code pushing, run [flake8](https://simpleisbetterthancomplex.com/packages/2016/08/05/flake8.html) for code styling and [isort](https://simpleisbetterthancomplex.com/packages/2016/10/08/isort.html) for organizing the python imports.

    docker-compose run app flake8
    docker-compose run app isort -rc .
