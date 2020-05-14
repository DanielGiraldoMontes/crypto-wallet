#!/usr/bin/env bash

echo "Waiting for MySQL..."

while ! nc -z db 3306; do
  sleep 0.5
done

echo "MySQL started"

flask db init
flask db migrate
flask db upgrade

# shellcheck disable=SC2164
cd /usr/src/app
python app.py run -h 0.0.0.0 -p 5000