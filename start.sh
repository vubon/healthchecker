#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn manage:app \
      --name verifier \
      --bind 0.0.0.0:5000 \
      --workers 3 \
      --access-logfile - --error-logfile - --log-level debug