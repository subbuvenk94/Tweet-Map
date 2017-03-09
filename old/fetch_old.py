import elasticsearch
from elasticsearch import Elasticsearch
import sys

es = Elasticsearch()

res = es.search(index="tweets", doc_type="tweet", body={"query": {"match": {"my_id": sys.argv[1]}}}, size=1000, from_=0)
print("%d tweets found\n" % res['hits']['total'])
list_of_tweets=''
for doc in res['hits']['hits']:
    list_of_tweets+="Username: %s\nHashTag: %s\nTweet: %s\n" % (doc['_source']['username'],doc['_source']['my_id'],doc['_source']['tweet'])
    list_of_tweets+='\n'
print list_of_tweets