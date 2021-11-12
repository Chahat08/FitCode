FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /django

COPY Pipfile Pipfile.lock /django/
RUN pip install pipenv && pipenv install --system

COPY . /django/