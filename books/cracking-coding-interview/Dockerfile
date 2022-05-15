FROM python:3.10.4

WORKDIR /src

ENV PYTHONPATH "${PYTHONPATH}:/src"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ src/
