from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import elasticsearch
from elasticsearch import Elasticsearch
import time
import json
import sys
import fetch

es = Elasticsearch()
con_key ='TQQvceMyQ8JpIp4yPDJ51eqkU'
con_secret ='tmdzEtXmD9dZhXfdt7hAUClL1ZC8efirBmhPYLztbb4iMzWIrL'
acess_token ='357005134-tlDx6j7FL3YfT749102zQcLU8uQ5ZlUj1KQxvkqc'
acess_secret = 'hp99szIiMvtOCvrDYDztPYCypJkBdLMtS4dfUuknyrRd0'

class listener(StreamListener):
    def on_data(self, raw_data):
        all_data = json.loads(raw_data)

        if 'text' in all_data:
            tweets = all_data["text"]
            username = all_data["user"]["screen_name"]
            location = all_data["user"]["location"]
            geo=all_data["geo"]
            coordinates=all_data["coordinates"]
            if geo!=None:
                doc = {
                        'time': time.time(),
                        'username': username,
                        'tweet': tweets,
                        'location': location,
                        'geo': geo,
                        'coordinates': coordinates
                        }
                es.index(index="tweets", doc_type='tweet', body=doc)
    # print("Tweet for %s added" % sys.argv[1])
    def on_error(self, status_code):
        print status_code

    def on_connect(self):
        print self

auth = OAuthHandler(con_key, con_secret)
auth.set_access_token(acess_token, acess_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["like","travel","better","good","love","today","work","football"])
# fetch(sys.argv[1])
# fetch.fetch(sys.argv[1])

# res = es.search(index="tweets", doc_type="tweet", body={"query": {"match": {"my_id": sys.argv[1]}}}, size=1000, from_=0)
# print("%d tweets found\n" % res['hits']['total'])
# list_of_tweets=''
# for doc in res['hits']['hits']:
#     list_of_tweets+="Username: %s\nHashTag: %s\nTweet: %s\n" % (doc['_source']['username'],doc['_source']['my_id'],doc['_source']['tweet'])
#     list_of_tweets+='\n'
# print list_of_tweets
