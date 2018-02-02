from flask import Flask

from tasks import count_tweets_task
from millo import *
from os.path import join

word_list = ["han", "hon", "den", "det", "denna", "denne", "hen"]
dir_path = '/mnt/tweets'
file_names = get_filenames(dir_path)

app = Flask(__name__)

@app.route('/millo', methods=['GET'])
def count_tweets_flask():
    #create a counting task
    for i, file_name in enumerate(file_names):
        file_path = join(dir_path,file_name)
        count_dict[i] = count_tweets_task.delay(file_path, word_list)






if __name__ == '__main__':
     app.run(host='0.0.0.0')
