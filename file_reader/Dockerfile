FROM python:3.13-rc-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

EXPOSE 8001

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \

COPY /src/file_reader_service.py .

CMD ["python", "file_reader_service.py"]