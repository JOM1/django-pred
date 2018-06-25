#!/bin/bash
sudo docker kill photoser
sudo docker rm photoser
sudo docker image rm photoser_img
sudo docker build -t photoser_img .
sudo docker run -d -p 8000:8000 --name photoser -e MINIO_IP=172.17.0.2 -e FLASK_IP=172.17.0.4 photoser_img

#sudo docker run -e MINIO_IP=172.17.0.2,FLASK_IP=172.17.0.3  -it photoser_img /bin/sh
