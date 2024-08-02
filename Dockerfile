FROM python:3.12.0-slim-buster

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry && \
  poetry config virtualenvs.create false && \
  poetry install --no-interaction --no-ansi

CMD [ "streamlit", "run", "./labmastro/main.py" ]