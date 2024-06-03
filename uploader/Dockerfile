from python:3.9 as base

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

FROM base as builder

COPY /uploader/ .

CMD ["python", "server.py"]
