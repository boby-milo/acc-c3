from flask import Flask, render_template

# from tasks import count_tweets_task
from millo import *
from os.path import join

word_list = ["han", "hon", "den", "det", "denna", "denne", "hen"]
# dir_path = '/mnt/tweets'
# file_names = get_filenames(dir_path)
dir_path = '../data'

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/tweets', methods=['GET'])
def tweets():
    render_template('tweets.html')
    html_path = './templates/bars.html'

    total_count = count_all_tweets(dir_path, word_list)
    visualize_tweets(total_count, html_path)
    return render_template('bars.html')

if __name__ == '__main__':
     app.config['TEMPLATES_AUTO_RELOAD'] = True
     app.run(host='0.0.0.0')
