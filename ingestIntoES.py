import json
from elasticsearch import Elasticsearch
from sys import stderr
import sys


def ingestIntoES(inputFileName):
    #es = Elasticsearch(["http" + '://'+"localhost" + ":" + str("9200")],show_ssl_warnings=False)
    es = Elasticsearch(["https" + '://'+ "darpamemex:darpamemex" + "@esc.memexproxy.com"],show_ssl_warnings=False)
    for line in open(inputFileName,'r'):
        if line.strip() != "":
            jsonurlobj = json.loads(line.strip())
            uri = jsonurlobj['uri']
            res = es.index(index="dig-unic-clusters-01",doc_type="ad",body=line)
            print("indexing id: " + res["_id"] + " for uri: " + str(uri))



if __name__ == '__main__':
    inputFileName = sys.argv[1]
    ingestIntoES(inputFileName)