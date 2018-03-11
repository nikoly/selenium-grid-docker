FROM python:3.6

ADD . /frontend-integration-tests

WORKDIR /frontend-integration-tests

RUN pip install -r requirements.txt

RUN chmod +x wait-for-it.sh
