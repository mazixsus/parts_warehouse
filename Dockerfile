FROM python:3.11-slim

# RUN apt-get update
# RUN apt-get install -y curl git gcc libpq-dev postgresql python3 musl
# RUN pip install --upgrade pip

ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.6.1
# ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /src /poetry

RUN pip install poetry==$POETRY_VERSION

COPY ./src/ ./src/
COPY ./poetry/ ./poetry/
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /poetry

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

WORKDIR /src

ENTRYPOINT ["/entrypoint.sh"]