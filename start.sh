#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
#python manage.py migrate
python manage.py collectstatic --no-input


echo "Flush the manage.py command it any"

while ! python manage.py flush --no-input 2>&1; do
  echo "Flusing django manage command"
  sleep 5
done

echo "Migrate the Database at startup of project"

# Wait for few minute and run db migraiton
while ! python manage.py migrate  2>&1; do
   echo "Migration is in progress status"
   sleep 5
done

python manage.py shell < config/create_user.py
echo "Django docker is fully configured successfully."

exec gunicorn healthchecker.wsgi:application -c ./config/gunicorn.config.py