FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
        binutils \
        libproj-dev \
        gdal-bin \
        wkhtmltopdf \
        && rm -rf /var/lib/apt/lists/*

WORKDIR /backend
COPY ./backend/requirements.txt /backend/requirements.txt
RUN pip install -r requirements.txt

COPY ./backend /backend
