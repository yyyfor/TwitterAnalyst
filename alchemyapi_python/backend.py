import sys
import time
from db import *
from search import *

def main(argv):
    db = DBO()
    table_topics = Topics(db)
    table_tweets = Tweets(db)
    tps = table_topics.get_topics()
    tws = TweetSearch()
    quota = 180
    while True:
        for (topic,_1,_2) in tps:
            for i in range(1,quota/len(tps)):
                print topic
                tweets = tws.search([topic])
                for tweet in tweets:
                    table_tweets.insert(
                            tweet['id'], topic, tweet['user']['id'], 
                            tweet['created_at'],tweet['favorite_count'], 
                            tweet['text'])
        time.sleep(600)
    db.close()
    


if __name__ == "__main__":
    main(sys.argv)
