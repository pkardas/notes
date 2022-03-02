FROM python:3.10.2

WORKDIR /architecture

ENV PYTHONPATH "${PYTHONPATH}:/architecture"

COPY requirements.txt .
COPY setup.cfg .

RUN pip install -r requirements.txt

COPY src/ src/
COPY tests/ tests/
