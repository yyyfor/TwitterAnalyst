import sys
import threading
from NLP import *
from DB import *
from GEO import *
import time


def GEOJOB():
    db = DBO()
    maps = GEO()
    table_tweets = Tweets(db)
    table_locations = Locations(db)
    while True:
        places = table_tweets.get_place()
        for place in places:
            (p,) = place
            cordinate = maps.geocode(p)
            if cordinate is not None:
                table_locations.insert(p,cordinate['lat'],cordinate['lng']) 
        time.sleep(120)

def NLPJOB():
    db = DBO()
    nlp = NLPEngine()
    table_tweets = Tweets(db)
    while True:
        tweets = table_tweets.get_tweets_wo_sentiment()
        for tweet in tweets:
            TWTID = tweet[0]
            text = tweet[5]
            score = nlp.sentiment(text)
            place = nlp.place(text)
            table_tweets.update_sentiment(TWTID, score)
            if place is not None:
                table_tweets.update_place(TWTID, place)
        time.sleep(60)

def main(argv):
    GEOThread = threading.Thread(target = GEOJOB)
    
    NLPThread = threading.Thread(target = NLPJOB)
    GEOThread.start()
    NLPThread.start()

    GEOThread.join()
    NLPThread.join()
        
if __name__ == "__main__":
    main(sys.argv)
