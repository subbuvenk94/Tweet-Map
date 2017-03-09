from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import elasticsearch
from elasticsearch import Elasticsearch
import time
import json
import sys

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

	doc = {
    		'time': time.time(),
    		'username': username,
    		'tweet': tweets,
            'location': location,
   			'my_id': sys.argv[1],
	}
	es.index(index="tweets", doc_type='tweet', body=doc)
    print("Tweet for %s added" % sys.argv[1])
    def on_error(self, status_code):
        print status_code

    def on_connect(self):
        print self

auth = OAuthHandler(con_key, con_secret)
auth.set_access_token(acess_token, acess_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#" + sys.argv[1]])
sys.exit()
