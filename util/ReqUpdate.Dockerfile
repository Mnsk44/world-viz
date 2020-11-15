FROM python:3.8

COPY requirements.in requirements.in
RUN pip3 install -r requirements.in

ENTRYPOINT [ "pip3", "freeze" ]