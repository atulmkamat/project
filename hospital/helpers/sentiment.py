import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


sid = SentimentIntensityAnalyzer()
def live_review(hotel_rev):
    sum=0
    for sentence in hotel_rev:
        print(sentence)
        ss = sid.polarity_scores(sentence)
        sum=sum+(ss["compound"])
    return sum
