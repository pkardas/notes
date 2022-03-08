FROM python:3.10.2

WORKDIR /src

ENV PYTHONPATH "${PYTHONPATH}:/src"

COPY requirements.txt .
COPY setup.cfg .

RUN pip install -r requirements.txt

COPY src/ src/
COPY tests/ tests/
