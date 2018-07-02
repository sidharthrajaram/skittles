import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.corpus import PlaintextCorpusReader
import random

corpus_root = 'corpus_files'
wordlists = PlaintextCorpusReader(corpus_root, '.txt')

corpus_list = ['addition.txt','subtraction.txt']

# ignore_words = stopwords.words('english')
def math_features(word):
    features = {}
    features["first_letter"] = word[0].lower()
    features["second_letter"] = word[1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count({})".format(letter)] = word.lower().count(letter)
        features["has({})".format(letter)] = (letter in word.lower())
    return features

# cfd = nltk.ConditionalFreqDist((fileid, word[1]) for fileid in corpus_list for word in wordlists.words(fileid))
# cfd.plot()

labeled_words = ([(word, 'addition') for word in wordlists.words('addition.txt')] + 
	[(word, 'subtraction') for word in wordlists.words('subtraction.txt')])

random.shuffle(labeled_words)

featuresets = [(math_features(n), operation) for (n, operation) in labeled_words]
train_set = featuresets[18:]
test_set = featuresets[:18]

print(labeled_words[18:])

classifier = nltk.NaiveBayesClassifier.train(train_set)

word = input("op word: ")
print('{} is {}'.format(word, classifier.classify(math_features(word))))

print(nltk.classify.accuracy(classifier, test_set))
# print(classifier.show_most_informative_features(5))