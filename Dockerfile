FROM python:3.11.4-bullseye
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR stock_password_generator
COPY requirements.txt .
RUN apt-get update \
    && apt-get -y install firebird-server
RUN pip install -r requirements.txt
COPY . .

CMD uvicorn main:app --port 80 --host 0.0.0.0
