import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.corpus import PlaintextCorpusReader

corpus_root = 'corpus_files'
wordlists = PlaintextCorpusReader(corpus_root, '.txt')
print(wordlists.words('addition.txt'))
print(wordlists.words('subtraction.txt'))

corpus_list = ['addition.txt','subtraction.txt']

# ignore_words = stopwords.words('english')

cfd = nltk.ConditionalFreqDist((fileid, word[0]) for fileid in corpus_list for word in wordlists.words(fileid))
cfd.plot()