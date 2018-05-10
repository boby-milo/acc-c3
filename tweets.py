from os import listdir
from os.path import isfile, join
import json
from bokeh.io import show, save, output_file
from bokeh.plotting import figure

WORD_LIST = ["han", "hon", "den", "det", "denna", "denne", "hen"]

def get_filenames(dir_path):
    file_names = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
    return file_names


def load_tweets_json(file_path):
    tweet_file = open(file_path)

    tweets = (line.rstrip() for line in tweet_file)
    tweets_json = (json.loads(line) for line in tweets if line)

    print "Tweets loaded from " + file_path + " file."
    return tweets_json


def count_word(word, tweets_json):
    word_counter = 0
    for tweet in tweets_json:
        tweet_txt = tweet['text']
        if key in tweet_txt:
            word_counter += 1
    return word_counter


def count_words(word_list, tweets_json, word_counter):
    for tweet in tweets_json:
        tweet_txt = tweet['text']

        for key in word_counter.keys():
            if key in tweet_txt:
                word_counter[key] += 1
    # print "Words counted: " + word_counter + "."
    # print word_counter
    return word_counter


def write_json(word_counter):
    word_counter_json = json.dumps(word_counter)
    print "\n\n\nFinal count: " + word_counter_json + "."
    outfile_name = 'word_count.json'
    with open(outfile_name, 'w') as outfile:
        json.dump(word_counter_json, outfile)
    print "Results saved to a JSON file " + outfile_name + "."


def count_tweets(file_path, word_list):
    word_count = dict(zip(word_list, [0] * len(word_list)))
    tweets_json = load_tweets_json(file_path)
    word_count = count_words(word_list, tweets_json, word_count)
    return word_count


def count_all_tweets(dir_path, word_list):
    word_count = dict(zip(word_list, [0] * len(word_list)))  # initialize
    file_names = get_filenames(dir_path)
    # print file_names

    for f in file_names[:10]:
        file_path = dir_path + '/' + f
        tweets_json = load_tweets_json(file_path)
        word_count = count_words(word_list, tweets_json, word_count)
    print word_count
    return word_count

def total_tweet_count(word_count_list, word_list):
    total_count = dict(zip(word_list, [0] * len(word_list)))
    for word_count in word_count_list:
        for word in word_list:
            total_count[word] += word_count[word]
    return total_count


def visualize_tweets(total_count, html_path):
    output_file(html_path)
    x = total_count.keys()

    p = figure(x_range=total_count.keys(), plot_height=500, title="Tweets",
               toolbar_location=None, tools="")

    p.vbar(x=total_count.keys(), top=total_count.values(), width=0.9)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    save(p)
    return 0


if __name__ == '__main__':
    word_list = ["han", "hon", "den", "det", "denna", "denne", "hen"]
    dir_path = '../data'
    file_name = '0c7526e6-ce8c-4e59-884c-5a15bbca5eb3'
    # file_name = get_filenames(dir_path)[0]
    file_path = join(dir_path, file_name)
    total_count = count_tweets(file_path, word_list)
    # print count_all_tweets(dir_path, word_list)
    print total_count
    a = visualize_tweets(total_count)
