


dig-Stylometry is a python library which helps you to compute signature for the data you have. 

What can you do with the signature ?
* You can use it for identifying documents which are similar.
* At ISI, we use it for finding similar advertisements in Human-Trafficking Domain which look alike. You will see examples below.


####Tools built with dig-Stylometry:
After getting the signature of documents, if you want to see which other documents have similar signature you can do clustering check 
[dig-tokenizer](https://github.com/usc-isi-i2/dig-tokenizer)
[dig-lsh-clustering]()

#### Requirements
* Spark: Visit http://spark.apache.org/downloads.html, select the package type of “Pre-built for Hadoop 2.4 and later,” and then click on the link for “Download Spark” This will download a compressed TAR file, or tarball. Uncompress the file into ```<spark-folder>```.
* Run `./make-spark.sh` every time to build the zip files required by spark every time you pull in new code
* Adding python path: To import pyspark module you have add pythonpath to your bash_profile file.<br />
you bash_profile file should look like :
```
export SPARK_HOME=/Users/rajagopal/Downloads/spark-1.5.2-bin-hadoop2.6
export PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH
export PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.8.2.1-src.zip:$PYTHONPATH
```

####How to install
pip install digStylometry

####Usage

```
python digStylometry/tests/testStylometry.py -i digStylometry/tests/text-json/input -o digStylometry/tests/text-json/output --file_format text

```
####Examples
To run this code, you have to give a config in the form of dictionary in the python script. Let's look at an example

```
  {` 
    "runlimit" : 5,
    "field" : "title_signature"
  }
```
What this means is 
*runLimit : you want to limit a run of same letters in the signature by fixed number of letters then use this option. For example, if the signature is WWWWWWWWWWDDDDDDDDDD and my runLimit is 5 then this will be changed to WWWWWDDDDD. More than 5 W's will be replaced by 5 W's.
*field : label of signature field   
  
#####Sample input
```
http://dig.isi.edu/ht/data/000010EFC2B9BB18B7CC864701FFBA5BD48D74EB/1369470540/webpage	"915-799-5634 ESCORT ALERT! -"
http://dig.isi.edu/ht/data/0000170FFCDE7DB5C0C52B0AF592175E3711A7B2/1353338700/webpage	"916-642-5533 - Escort Ad -"
```
Input should be in 
```<key> <value>```

#####Sample output
```
http://dig.isi.edu/ht/data/000010EFC2B9BB18B7CC864701FFBA5BD48D74EB/1369470540/webpage	{"title_signature": "DDD-DDD-DDDDLLLLL!-"}
http://dig.isi.edu/ht/data/0000170FFCDE7DB5C0C52B0AF592175E3711A7B2/1353338700/webpage	{"title_signature": "DDD-DDD-DDDD-LwwwwwLw-"}
```
Output will be in the form of 
```<key> <signature>```

####How the signature is derived ?
Intially on the value some preprocessing is done like removing the HTML tags and then replaces alphabets with specific letters and digits with D.

1. All single uppercase letters are replaced with 'L'
2. Words with all capitals are replaced with 'W' by each letter
3. First letter is capital and all others are small are replaced with 'C'
4. All words with lowercase letters are replaced with 'w'
5. All digits are replaced with 'D'


You can modify the [code for signature](https://github.com/usc-isi-i2/dig-stylometry/blob/devel/digStylometry/Stylometry.py#L82) as per your requirement by cloning this repo.


If you want to report bugs or suggest improvements you can mail to dig-isi@isi.edu
