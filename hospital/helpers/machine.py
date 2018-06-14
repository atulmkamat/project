import nltk
import pickle
from nltk.stem import WordNetLemmatizer
from sklearn.externals import joblib
import numpy as np

wordnet_lemmatizer = WordNetLemmatizer()
stopwords = set(w.rstrip() for w in open('/home/atul/Desktop/easclepius/easclepius/stopwords.txt'))

pickle_in = open("/home/atul/Desktop/easclepius/easclepius/wim","rb")
word_index_map = pickle.load(pickle_in)

loaded_model = joblib.load('/home/atul/Desktop/easclepius/easclepius/finalized_model.sav')

#live_reviews= BeautifulSoup(open('live.txt').read())
#live_reviews=live_reviews.findAll('review_text')

live_tokenized = []

result=0

live_data = np.zeros((1, (len(word_index_map)+1)))

def my_tokenizer(s):
    s = s.lower() # downcase
    tokens = nltk.tokenize.word_tokenize(s) # string to tokens
    tokens = [t for t in tokens if len(t) > 2] # remove short words
    tokens = [wordnet_lemmatizer.lemmatize(t) for t in tokens] # put words into base form
    tokens = [t for t in tokens if t not in stopwords] # remove stopwords
    return tokens

def tokens_to_vector(tokens, label):
    x = np.zeros(len(word_index_map) + 1) 
    for t in tokens:
        i = word_index_map[t]
        x[i] += 1
    x = x / x.sum() 
    x[-1] = label
    return x

def analyze(rev):
#for review in live_reviews:
    zoken=my_tokenizer(rev)
    live_tokenized.append(zoken)

    for tokens in live_tokenized:
        xd = tokens_to_vector(tokens, 1)
        live_data[0,:] = xd

    Z=live_data[:,:-1]

    print ("your review is: ")
    m=loaded_model.predict(Z)
    conf=loaded_model.decision_function(Z)
    print(conf)
    print(m[0])
    a=m[0]
    print(type(bool(a)))
    return a
