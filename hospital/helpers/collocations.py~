import nltk
from nltk.collocations import *
from nltk.corpus import stopwords
from nltk.corpus import webtext
from nltk.corpus import PlaintextCorpusReader
import numpy as np
from nltk import FreqDist
from sklearn.linear_model import LogisticRegression
from bs4 import BeautifulSoup
count=0

def give(filename):
 corpus_root = '/home/helios/Desktop/easclepius/easclepius'
 wordlists = PlaintextCorpusReader(corpus_root, '.*') 

 name="/home/helios/Desktop/easclepius/easclepius/"+filename
 print (filename)
 print(name)
 print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
 textwords=[w.lower() for w in wordlists.words(name)]
 print (textwords)
 bigram_measures = nltk.collocations.BigramAssocMeasures()
 finder=BigramCollocationFinder.from_words(textwords)


 finder.apply_freq_filter(2)
 ignored_words = set(stopwords.words('english'))
 finder.apply_word_filter(lambda w: len(w) < 3 or w in ignored_words)
 a=finder.nbest(bigram_measures.likelihood_ratio,5)
 fd=FreqDist(a)
 print("fd")
 return a
