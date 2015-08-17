import sys
import json
from TwitterSearch import *
class TweetSearch:
    def __init__(self):
        self.ts = TwitterSearch(
                consumer_key = 'uVp0jLzC043jvVxsoYtO7XnTy',
                consumer_secret = 'zHHqf6gaRGeLX9PS4YB4BMhcUo7p8dyI02cZLxVQOTnoHEG0gh', 
                access_token = '247768860-1BdrGZgXQibjaDSiZxGQ1MbjCxCEsM85gDFnRMjr',
                access_token_secret = 'ImetdaaKxq4uMvkQiMIxbGiR92ywqjYas52EZSXOyPu1t')
               # consumer_key = 'zTY2l3OYf9n50WgPG6KOCcr3J',
               # consumer_secret = 'sHqr1o1bCmW5xqPQE6wA7wCwsti00kT6hDnM6SlHNIr2kqStiJ', 
               # access_token = '597976696-zDOpw9mCLkJ05JKXemq9OAJ1qf6pjVg0G4zhtCrl',
               # access_token_secret = 'lmiwWH69u5MfDGWNhXaFlcyo4882uN2Fm7dYxcAPVPaAq')

    def search(self,keywords):
        print keywords
        tso = TwitterSearchOrder()
        tso.set_keywords(keywords)
        tso.set_language('en')
        tso.set_include_entities(False)
        tweets = None
        try:
            tweets = self.ts.search_tweets_iterable(tso)
            print tweets
        except TwitterSearchException as e: # catch all those ugly errors
            print(e)
        return tweets

if __name__ == "__main__":
    tws = TweetSearch()
    for tweet in tws.search([sys.argv[1]]):
        print tweet['id'], sys.argv[1], tweet['user']['id'], tweet['created_at'], tweet['favorite_count'], tweet['text']
        #print json.dumps(tweet, indent=4)
