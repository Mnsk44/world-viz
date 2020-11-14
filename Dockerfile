FROM python:3.8

COPY world-viz/ /app/world-viz
WORKDIR /app

RUN ["python3", "/app/world-viz/main.py"]