#!/bin/sh

echo "I'm alive!"

mkdir ~/millo
sudo mkdir /mnt/tweets
sudo mount /dev/vdb1 /mnt/tweets
sudo chown ubuntu:ubuntu /mnt/tweets

sudo apt-get update -y
sudo apt-get upgrade -y

echo "Installing pip..."
sudo apt-get install -y python-pip
sudo -H pip install --upgrade pip

echo "Installing rabbitmq..."
sudo apt-get install -y rabbitmq-server
sudo service rabbitmq-server restart

echo "Installing celery..."
sudo -H pip install celery

# echo "Installing flask..."
# sudo -H pip install Flask

echo "Installing django..."
sudo -H pip install django

echo "Installing milo..."
cd /home/ubuntu
sudo git clone https://github.com/millovanovic/acc-c3.git
cd /home/ubuntu/acc-c3/
sudo git checkout django
sudo python manage.py migrate

echo "Starting django..."
sudo screen -S djangoserver -d -m bash -c 'python manage.py runserver 0:8000'

echo "Initialization complete!"