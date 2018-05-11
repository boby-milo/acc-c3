from celery import Celery
from flask import Flask, render_template
from time import sleep
from tweets import *

DIR_PATH = '/mnt/tweets'

def make_celery(app):
    celery_app = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery_app.conf.update(app.config)

    class ContextTask(celery_app.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app.Task = ContextTask
    return celery_app

flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL='amqp://localhost',
    CELERY_RESULT_BACKEND='rpc://'
)
celery_app = make_celery(flask_app)

@celery_app.task()
def add_together(a, b):
    return a + b

@celery_app.task()
def count_file(file_path, word_list):
    word_count = count_tweets(file_path, word_list)
    return word_count




@flask_app.route('/', methods=['GET'])
def index():
	return render_template('index.html')


@flask_app.route('/tweets', methods=['GET'])
def tweets():
    word_list = WORD_LIST
    dir_path = DIR_PATH
    html_path = './templates/bars.html'
    file_names = get_filenames(dir_path)
    word_count_task = []
    for file_name in file_names:
        file_path = join(dir_path, file_name)
        word_count_task.append(count_file.delay(file_path, word_list))
        print "Task submitted!"

    word_count_list = len(word_count_task) * [0]
    counting_done = False
    counter = 0
    while not counting_done:
        counter += 1
        counting_done = True
        for ii, wct in enumerate(word_count_task):
            if wct.successful():
                print("Task " + str(ii) + " has finished, status: " + str(wct.status))
                word_count_list[ii] = wct.result;
            else:
                print("Task " + str(ii) + " has not finished yet, status: " + str(wct.status))
                counting_done = False
        sleep(5)

    print "Counting done!"

    total_count = total_tweet_count(word_count_list, word_list)
    visualize_tweets(total_count, html_path)
    return render_template('bars.html')
