import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.corpus import PlaintextCorpusReader
import random
from nltk import word_tokenize

corpus_root = 'corpus_files'
wordlists = PlaintextCorpusReader(corpus_root, '.txt')

# corpus_list = ['addition.txt','subtraction.txt']
# cfd = nltk.ConditionalFreqDist((fileid, word[0]) for fileid in corpus_list for word in wordlists.words(fileid))
# cfd.plot()
ignore_words = stopwords.words('english')
ignore_symbols = ['!','.',',',';',':','?','#','-']

def math_features(word):
    features = {}
    features["first_letter"] = word[0].lower()
    features["second_letter"] = word[1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count({})".format(letter)] = word.lower().count(letter)
        features["has({})".format(letter)] = (letter in word.lower())
    return features

def get_features(word):
	return {'first letter': word[0]}

def trained_model():
	labeled_words = ([(word, 'addition') for word in wordlists.words('addition.txt')] + 
		[(word, 'subtraction') for word in wordlists.words('subtraction.txt')])
	random.shuffle(labeled_words)
	featuresets = [(get_features(n), operation) for (n, operation) in labeled_words]
	train_set = featuresets[19:]
	test_set = featuresets[:19]

	classifier = nltk.NaiveBayesClassifier.train(train_set)
	return classifier, test_set

def preprocess(sentence):
	sent = word_tokenize(sentence)
	clean = []
	for word in sent:
		if(word.lower() not in ignore_words and word.lower() not in ignore_symbols):
			clean.append(word)
	return clean

def getNumbers(clean):
	leftovers = []
	numbers = []
	for word in clean:
			try: 
				num = int(word)
				numbers.append(str(num))
			except(ValueError):
				leftovers.append(word)
				pass
	return numbers, leftovers

def getOperators(words):
	tagged_words = nltk.pos_tag(words)
	to_classify = []
	for word in tagged_words:
		if 'V' in word[1]:
			to_classify.append(word[0])
	return to_classify
if __name__ == '__main__':

	classifier = trained_model()[0]
	test_set = trained_model()[1]
	print('Accuracy: {}'.format(nltk.classify.accuracy(classifier, test_set)))

	sentence = input("word problem: ")
	cleaned = preprocess(sentence)
	numbers = getNumbers(cleaned)[0]
	print(numbers)
	leftovers = getOperators(getNumbers(cleaned)[1])
	for word in leftovers:
		print('{} is {}'.format(word, classifier.classify(get_features(word))))






















