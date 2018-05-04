from flask import Flask, render_template

# from tasks import count_tweets_task
from millo import *
from os.path import join

word_list = ["han", "hon", "den", "det", "denna", "denne", "hen"]
# dir_path = '/mnt/tweets'
# file_names = get_filenames(dir_path)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/tweets', methods=['GET'])
def tweets():
    #create a counting task
#     for i, file_name in enumerate(file_names):
#         file_path = join(dir_path,file_name)
#         count_dict[i] = count_tweets_task.delay(file_path, word_list)
    return render_template('tweets.html')

if __name__ == '__main__':
     app.config['TEMPLATES_AUTO_RELOAD'] = True
     app.run(host='0.0.0.0')
