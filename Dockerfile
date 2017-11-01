FROM python:2.7
MAINTAINER Walter T. Hiranpat <whiranpat@mitre.org>
VOLUME ["/tmp"]
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["/bin/bash","start.sh"]
