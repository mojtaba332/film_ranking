FROM python:latest

RUN pip install --upgrade pip
RUN pip install flask-cors
ENTRYPOINT flask --app main run --host=0.0.0.0 --debug