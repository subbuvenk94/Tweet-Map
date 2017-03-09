import elasticsearch
from elasticsearch import Elasticsearch
import sys

es = Elasticsearch(['54.201.211.220:9200'])
def fetch(keyword):
    res = es.search(index="tweets", doc_type="tweet", body={"query": {"match": {"tweet": keyword}}}, size=1000, from_=0)
    print("%d tweets found\n" % res['hits']['total'])
    list_of_tweets=[]
    for doc in res['hits']['hits']:
        list_of_tweets.append([doc['_source']['tweet'],doc['_source']['geo']['coordinates'][0], doc['_source']['geo']['coordinates'][1]])
    if not list_of_tweets:
        return None
    return list_of_tweets
