import sys
import json
import itertools

def createGroundTruth(inputFileName,outputFileName):
    inputFile = open(inputFileName,'r')
    outputFile = open(outputFileName,'w')
    jsonObj = json.load(inputFile)
    clusters = jsonObj['aggregations']['clusteragg']['buckets']
    for cluster in clusters:
        uri_list = []
        ads = cluster['sampleads']['hits']['hits']
        for ad in ads:
            uri_list.append(ad['_source']['uri'])
        pairs = itertools.combinations(uri_list,2)
        for uri in pairs:
            outputFile.write(str(uri) + "\n")
    outputFile.close()




if __name__ == '__main__':
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
    createGroundTruth(inputFileName,outputFileName)

