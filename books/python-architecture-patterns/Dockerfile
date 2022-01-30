FROM python:3.10.2

WORKDIR /architecture

COPY requirements.txt .
COPY setup.cfg .

RUN pip install -r requirements.txt

COPY src/ .
COPY tests/ .
