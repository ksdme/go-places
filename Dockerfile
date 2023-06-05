FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install && \
    poetry run ./manage.py collectstatic
CMD [ "/app/bin/run.sh" ]
