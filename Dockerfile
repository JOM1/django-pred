FROM registry.access.redhat.com/rhscl/python-36-rhel7

WORKDIR /photoSer
COPY . /photoSer
RUN pip3 install pipdeps/*
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

