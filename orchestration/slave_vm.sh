#!/bin/sh

echo "This slave is alive!"

echo "Mounting the data..."
sudo mkdir /mnt/tweet_data
sudo mount /dev/vdb1 /mnt/tweet_data
sudo chown ubuntu:ubuntu /mnt/tweet_data

sudo apt-get update -y
sudo apt-get upgrade -y

echo "Installing pip..."
sudo apt-get install -y python-pip
sudo -H pip install --upgrade pip
sudo -H pip install numpy

echo "Installing celery..."
sudo -H pip install celery

echo "Installing django..."
sudo -H pip install django

echo "Installing milo..."
cd /home/ubuntu
sudo git clone https://github.com/millovanovic/acc-c3.git
cd /home/ubuntu/acc-c3/
sudo git checkout master

echo "Setting permission"
sudo chown -R ubuntu.users /home/ubuntu/acc-c3

echo "Connecting to the main rabbitmq node..."
sudo sed 's/localhost/MASTER_IP/' -i /home/ubuntu/acc-c3/milotweet/settings.py

echo "Starting celery worker..."
cd /home/ubuntu/acc-c3/
sleep 5
sudo screen -S celeryserver -d -m bash -c 'sudo -u ubuntu celery worker -A milotweet -l info'

echo "Initialization complete!"
