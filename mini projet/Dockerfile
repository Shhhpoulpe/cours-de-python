FROM python:3.6-slim

WORKDIR /usr/src/app

COPY . .

RUN apt-get update && apt-get install -y \
    vim \
    python \
    python-pip
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python","app.py"]