#!/usr/bin/bash

set -e -x

poetry run migrate

poetry run gunicorn app.wsgi
