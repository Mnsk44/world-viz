FROM world-viz:latest as base

COPY test test
COPY util/test_requirements.txt test_requirements.txt

RUN pip3 install -r test_requirements.txt && \
    rm -rf test_requirements.txt

# Reset parent entrypoint for now
ENTRYPOINT []