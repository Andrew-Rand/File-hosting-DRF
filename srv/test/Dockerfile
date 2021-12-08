FROM python:3.8.10

#Main project directory in container
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#copy files to . (WORKDIR in container)
COPY Pipfile .
COPY Pipfile.lock .

#first command in container terminal
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
