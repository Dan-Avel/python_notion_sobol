# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app
RUN apt-get -y update
RUN pip3 install -r requirements.txt
ENV sobol_api_key=''
ENV notion_api_key=''
ENV notion_db_id=''
CMD python3 -m src