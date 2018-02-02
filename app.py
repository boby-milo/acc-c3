from flask import Flask
from millo import *


word_list = ["han", "hon", "den", "det", "denna", "denne", "hen"]
dir_path = '/mnt/tweets'
file_names = get_filenames(dir_path)

if __name__ == '__main__':
     app.run(host='0.0.0.0')
