#!/bin/bash

set -e

python manage.py migrate --no-input
python manage.py collectstatic --no-input

exec gunicorn core.wsgi:application \
  -b 0.0.0.0:8000 \
  --workers 3 \
  --threads 3 \
  --no-control-socket