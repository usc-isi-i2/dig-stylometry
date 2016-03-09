try:
    from pyspark import SparkContext
except:
    print "### NO PYSPARK"
from digSparkUtil.dictUtil import as_dict, dict_minus
from digSparkUtil.fileUtil import FileUtil
import argparse
from digStylometry import ComputeSignature

def testSignature(sc,inputFileName,outputFileName,file_format):

    config = {
    "runlimit" : 5,
    "field" : "title_signature"
    }

    fUtil = FileUtil(sc)
    rdd = fUtil.load_file(inputFileName,file_format=file_format,data_type="json")
    signature = ComputeSignature(**config)
    rdd = signature.perform(rdd)

    fUtil.save_file(rdd,outputFileName,file_format="text",data_type="json")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--inputFile",help = "input File path",required=True)
    parser.add_argument("-o","--output_dir",help = "output File path",required=True)
    parser.add_argument("--file_format",help = "file format text/sequence",default='sequence')


    args = parser.parse_args()
    sc = SparkContext(appName="Stylometry")
    testSignature(sc,args.inputFile,args.output_dir,args.file_format)