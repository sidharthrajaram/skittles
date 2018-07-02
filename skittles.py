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
ignore_words.append('had')
ignore_words.append('has')
ignore_words.append('owned')
ignore_words.append('owns')

ignore_symbols = ['!','.',',',';',':','?','#','-']

def get_features(word):
	return {'first letter': word[0]}

def trained_model():
	labeled_words = ([(word, 'addition') for word in wordlists.words('addition.txt')] + 
		[(word, 'subtraction') for word in wordlists.words('subtraction.txt')])
	random.shuffle(labeled_words)
	featuresets = [(get_features(n), operation) for (n, operation) in labeled_words]
	train_set = featuresets[21:]
	test_set = featuresets[:21]

	classifier = nltk.NaiveBayesClassifier.train(train_set)
	return classifier, test_set

def translate(sentence):
	translated = ''
	classifier = trained_model()[0]
	test_set = trained_model()[1]
	print('Accuracy: {}'.format(nltk.classify.accuracy(classifier, test_set)))
	tokenized = word_tokenize(sentence)
	pos = nltk.pos_tag(tokenized)
	for word in pos:
		if(word[1]=='CD'):
			translated+= ' '+word[0]
		elif('V' in word[1] and word[0] not in ignore_words):
			verb = word[0]
			op = classifier.classify(get_features(verb))
			if(op=='addition'):
				translated += ' '+'+'
			else:
				translated += ' '+'-'
	return translated

if __name__ == '__main__':
	sentence = input("word problem: ")
	print(translate(sentence))





















