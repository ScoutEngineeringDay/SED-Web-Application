#!/bin/bash

clear 

echo "Running python manage.py makemigrations"

python manage.py makemigrations

echo "python manage.py makemigrations DONE!"

echo "Running python manage.py migrate"

python manage.py migrate

echo "python manage.py migrate DONE!"

echo "Running python manage.py runserver 0.0.0.0:8000"

python manage.py runserver 0.0.0.0:8000

echo "python manage.py runserver 0.0.0.0:8000 DONE!"
