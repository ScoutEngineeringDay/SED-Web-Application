#!/bin/bash
python manage.py check
ready=$?
while [ $ready -ne 0 ]; do sleep 1; python manage.py check; ready=$?; done
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000