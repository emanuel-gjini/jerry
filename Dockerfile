FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /codebase
COPY requirements.txt /codebase/
RUN pip3 install -r requirements.txt
COPY . /codebase/