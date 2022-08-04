FROM tiangolo/uvicorn-gunicorn:python3.8-slim

COPY ./requirement.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app

COPY . .


