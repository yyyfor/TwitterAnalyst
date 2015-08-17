import sys
import time
from DB import *
from TweetsClaw import *

def main(argv):
    db = DBO()
    table_topics = Topics(db)
    table_tweets = Tweets(db)
    tws = TweetSearch()
    quota = 180
    while True:
        for i in range(1,quota):
            tps = table_topics.get_topics()
            for (topic,_1,_2) in tps:
                tweets = tws.search([topic])
                counter = 0
                for tweet in tweets:
                    counter += 1
                    table_tweets.insert(
                                tweet['id'], topic, tweet['user']['id'], 
                                tweet['created_at'],tweet['favorite_count'], 
                                tweet['text'])
                    print counter
                    if counter == 100:
                        break
        time.sleep(600)
    db.close()

if __name__ == "__main__":
    main(sys.argv)
