try:
    from pyspark import SparkContext
except:
    print "### NO PYSPARK"
from digSparkUtil.dictUtil import as_dict, dict_minus
from digSparkUtil.fileUtil import FileUtil

def convert(sc,inputFileName,outputFileName):
    fileUtil = FileUtil(sc)
    rdd = fileUtil.load_file(inputFileName,file_format="text",data_type="json")
    fileUtil.save_file(rdd,outputFileName)


if __name__ == '__main__':
    inputFileName = "/Users/rajagopal/Desktop/github_repos/dig-stylometry/digStylometry/tests/text-json/input"
    outputFileName = "/Users/rajagopal/Desktop/github_repos/dig-stylometry/digStylometry/tests/sequence-json/input1"
    sc = SparkContext(appName="TEST")
    convert(sc,inputFileName,outputFileName)
