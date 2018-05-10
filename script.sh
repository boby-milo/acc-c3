#!/bin/bash

# exec 3>&1 4>&2
# trap 'exec 2>&4 1>&3' 0 1 2 3
# exec 1>log.out 2>&1

rabbitmq-server restart &>rabbit.log &

screen -S celery -d -m bash -c 'celery -A backend.celery_app worker'
celery -A backend status

screen -S flower -d -m bash -c 'celery -A backend flower'

screen -S flask -d -m bash -c 'python millo.py'

echo "millo is deployed!"

# celery -A tasks control shutdown
