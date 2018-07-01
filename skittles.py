import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.corpus import PlaintextCorpusReader
import random

corpus_root = 'corpus_files'
wordlists = PlaintextCorpusReader(corpus_root, '.txt')

corpus_list = ['addition.txt','subtraction.txt']

# ignore_words = stopwords.words('english')

cfd = nltk.ConditionalFreqDist((fileid, word[0]) for fileid in corpus_list for word in wordlists.words(fileid))
# cfd.plot()

def math_features(word):
	return {'last_letter': word[0]}

labeled_words = ([(word, 'addition') for word in wordlists.words('addition.txt')] + 
	[(word, 'subtraction') for word in wordlists.words('subtraction.txt')])

random.shuffle(labeled_words)

featuresets = [(math_features(n), operation) for (n, operation) in labeled_words]
train_set = featuresets[13:]
test_set = featuresets[:13]

classifier = nltk.NaiveBayesClassifier.train(train_set)

word = 'additionally'
print(classifier.classify(math_features(word)))