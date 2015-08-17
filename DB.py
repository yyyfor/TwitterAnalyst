import mysql.connector
import datetime
from sets import Set
class DBO:
    def __init__(self):
        self.cnx = mysql.connector.connect(
                user='zw627',
                password = 'zw627123',
                host= '127.0.0.1',
                port= '3307',
                database = 'zw627')
    def close(self):
        self.cnx.close()

class Topics:
    def __init__(self, dbo):
        self.dbo = dbo
    def insert_topic(self, topic):
        pass
    def update_time(self, topic):
        try:
            cursor = self.dbo.cnx.cursor()
            cursor.execute("UPDATE Topics SET last_update = now() WHERE topic = '%s'" % (topic))
            self.dbo.cnx.commit()

        except mysql.connector.Error as err:
            print("update_time: {}".format(err))
        finally:
            cursor.close()
    
    def get_topics(self):
        topics = Set()
        try:
            cursor = self.dbo.cnx.cursor()
            cursor.execute("SELECT * FROM Topics")
            for topic in cursor:
                topics.add(topic)
        except mysql.connector.Error as err:
            print("get_topics: {}".format(err))
        finally:
            cursor.close()
        return topics

class Tweets:
    def __init__(self,dbo):
        self.dbo = dbo
    def insert(self, twtid, topic, user_id, created_at, favorite_count, text):
        print("%s  %s %s  %s %s  %s") % (twtid, topic, user_id, created_at, favorite_count, text)
        try:
            cursor = self.dbo.cnx.cursor()
            tst = datetime.datetime.strptime(created_at, "%a %b %d %H:%M:%S +0000 %Y")
            query = "INSERT INTO Tweets(TWTID, topic, user_id,created_at, favorite_count, text) VALUES(%s,%s,%s,%s, %s,%s)"
            data = (twtid, topic,user_id, tst.strftime('%Y-%m-%d %H:%M:%S'), favorite_count, text)
            cursor.execute(query,data)
            self.dbo.cnx.commit()
        except mysql.connector.Error as err:
            print("insert : {}".format(err))
        finally:
            cursor.close()
    def get_tweets_wo_sentiment(self):
        cursor = self.dbo.cnx.cursor()
        try:
            cursor.execute("SELECT * FROM Tweets WHERE sentiment is null")
            tweets = Set()
            for tweet in cursor:
                tweets.add(tweet)
        except mysql.connector.Error as err:
            print("get_tweets_wo_sentiment: {}".format(err))
        finally:
            cursor.close()
        return tweets

    def get_place(self):
        tweets = Set()
        try:
            cursor = self.dbo.cnx.cursor()
            cursor.execute("SELECT place FROM Tweets GROUP BY place having place is not null")
            for tweet in cursor:
                tweets.add(tweet)
        except mysql.connector.Error as err:
            print("get_place: {}".format(err))
        finally:
            cursor.close()
        return tweets

    def update_sentiment(self,twtid,score):
        try:
            cursor = self.dbo.cnx.cursor()
            cursor.execute("UPDATE Tweets SET sentiment='%s' WHERE TWTID='%s'" % (score,twtid))
            self.dbo.cnx.commit()

        except mysql.connector.Error as err:
            print("update_sentiment: {}".format(err))
        finally:
            cursor.close()
    def update_place(self,twtid,place):
        try:
            cursor = self.dbo.cnx.cursor()
            cursor.execute("UPDATE Tweets SET place='%s' WHERE TWTID='%s'" % (place,twtid))
            self.dbo.cnx.commit()

        except mysql.connector.Error as err:
            print("update_sentiment: {}".format(err))
        finally:
            cursor.close()

 
class Locations:
    def __init__(self,dbo):
        self.dbo = dbo
    def insert(self,place, lat , lng):
        print place
        print lat,lng
        try:
            cursor = self.dbo.cnx.cursor()
            query =  "INSERT INTO Locations(place, latitude, longitude) VALUES(%s,%s,%s)"
            data = (place,lat,lng)
            cursor.execute(query,data)
            self.dbo.cnx.commit()
        except mysql.connector.Error as err:
            print("insert: {}".format(err))
        finally:
            cursor.close()

