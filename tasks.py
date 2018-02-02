from celery import Celery
from millo import *

app = Celery('proj',
                broker = 'amqp://user1:pwd@localhost:5672/vhost1',
                backend = 'amqp://user1:pwd@localhost:5672/vhost1')
                # include = ['tasks'])

@app.task
def count_tweets_task(file_path, word_list):
    return count_tweets(file_path, word_list)

if __name__ == "__main__":
    app.start()
