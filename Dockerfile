FROM python:alpine3.7

RUN pip3 install django boto3 botocore
COPY . /photoSer
WORKDIR /photoSer
EXPOSE 8000
CMD python3 manage.py runserver

