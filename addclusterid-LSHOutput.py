import sys
import ast
import json

#adds a cluster uri by hashing all the uris in the cluster
def modifyJSON(inputFileName):
    inputFile = open(inputFileName,'r')
    outputFile = open(outputFileName,'w')
    for line in inputFile:
        jsonObj = ast.literal_eval(line)
        items = jsonObj['cluster']
        concat_str = ''
        for item in items:
            concat_str += item['uri']
        cluster_id = "http://dig.isi.edu/ht/data/" + str(hash(concat_str)% 982451653 )
        for item in items:
            item['cluster_id'] = cluster_id
            outputFile.write(json.dumps(item) + "\n")
    inputFile.close()
    outputFile.close()


if __name__ == '__main__':
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
    modifyJSON(inputFileName)