#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
python manage.py migrate
python manage.py collectstatic --no-input
exec gunicorn healthchecker.wsgi:application \
      --name verifier \
      --bind 0.0.0.0:8000 \
      --workers 3 \
      --access-logfile - --error-logfile - --log-level debug