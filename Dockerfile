FROM python:3.8-slim-buster

WORKDIR app/


RUN pip install -U pip && pip install poetry

COPY ./poetry-env/poetry.lock ./poetry-env/pyproject.toml ./

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction

COPY . ./

EXPOSE 80

RUN chmod 777 ./initialize.sh 

ENTRYPOINT ["./initialize.sh"]