from celery import Celery
from millo import *

app = Celery('tasks',
                broker = 'amqp://localhost',
                backend = 'amqp://localhost')
                # include = ['tasks'])

@app.task
def count_tweets_task(file_path, word_list):
    return count_tweets(file_path, word_list)

if __name__ == "__main__":
    app.start()
