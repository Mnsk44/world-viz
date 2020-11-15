FROM python:3.8 as production

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt && \
    rm -rf requirements.txt

COPY world-viz/ world-viz

ENTRYPOINT ["python3", "world-viz/main.py"]

# Populate DB with submodule for now
FROM production as db_population
COPY data/ data/

ENTRYPOINT [ "python3", "world-viz/db_populate/populate.py" ]