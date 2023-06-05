#!/bin/bash

set -e -x

poetry run ./manage.py migrate

poetry run gunicorn --bind 0.0.0.0:8000 app.wsgi
