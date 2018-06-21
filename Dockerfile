FROM python:alpine3.7

WORKDIR /photoSer
RUN apk update ; apk add git ; git clone https://github.com/JOM1/django-pred.git /photoSer
RUN pip3 install pipdeps
EXPOSE 8000
CMD ["python3", "manage.py", "runserver"]

