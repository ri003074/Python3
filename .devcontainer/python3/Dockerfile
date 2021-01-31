FROM python:3.8-slim
WORKDIR /tmp/py
COPY requirements.txt ${PWD}
RUN pip install -r requirements.txt
RUN apt-get -y update && apt-get -y install git