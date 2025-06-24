FROM python:3.12

WORKDIR /app

COPY . .

RUN mkdir -p tests && touch tests/__init__.py
