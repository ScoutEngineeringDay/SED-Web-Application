FROM python:2.7
MAINTAINER Walter T. Hiranpat <whiranpat@mitre.org>
VOLUME ["/tmp"]
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "collectstatic"]
CMD ["python", "manage.py", "syncdb", "--noinput"]
CMD ["python", "manage.py", "migrate", "--noinput"]
CMD ["python","manage.py","runserver","0.0.0.0:8000"]



