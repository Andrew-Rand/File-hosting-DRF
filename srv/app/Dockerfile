FROM python:3.8.10

#Main project directory in container
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#copy files to . (WORKDIR in container)
COPY Pipfile .
COPY Pipfile.lock .
#  add entrypoint.sh to porject
COPY entrypoint.sh .

#first command in container terminal
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

#copy important into container
COPY ./src .
COPY ./manage.py .
COPY ./static .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
