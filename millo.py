from os import listdir
from os.path import isfile, join
import json

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
	print word_counter
	return word_counter

def write_json(word_counter):
	word_counter_json = json.dumps(word_counter)
	print "\n\n\nFinal count: " + word_counter_json + "."
	outfile_name = 'word_count.json'
	with open(outfile_name, 'w') as outfile: json.dump(word_counter_json, outfile)
	print "Results saved to a JSON file " + outfile_name + "."

def count_tweets(file_path, word_list):
	word_count = dict(zip(word_list, [0] * len(word_list)))
	tweets_json = load_tweets_json(file_path)
	word_count = count_words(word_list, tweets_json, word_count)
	return word_count

# def count_all_tweets(dir_path):
# 	word_list = ["han", "hon", "den", "det", "denna", "denne", "hen"]
# 	word_count = dict(zip(word_list, [0] * len(word_list))) #initialize
#
# 	file_names = get_filenames(dir_path)
# 	print file_names
#
# 	for f in file_names:
# 		file_path = dir_path+'/'+f
# 		tweets_json = load_tweets_json(file_path)
# 		word_count = count_words(word_list, tweets_json, word_count)
#
# 	write_json(word_count)
# 	return "Tweets counted!"

if __name__ == '__main__':
	word_list = ["han", "hon", "den", "det", "denna", "denne", "hen"]
	dir_path = '../data'
	# file_name = '0c7526e6-ce8c-4e59-884c-5a15bbca5eb3'
	file_name = get_filenames(dir_path)[0]
	file_path = join(dir_path,file_name)
	count_tweets(file_path, word_list)
