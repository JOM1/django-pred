#!/bin/bash
sudo docker kill photoser
sudo docker rm photoser
sudo docker image rm photoser_img
sudo docker build -t photoser_img .
#sudo docker run -d  -p 8000:8000 --name photoser photoser_img

sudo docker run -it photoser_img /bin/sh
