#!/bin/bash
sudo docker run -d -p 27017:27017 mongo
sudo docker run -d -p 5672:5672 rabbitmq
