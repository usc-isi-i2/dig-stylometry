#!/bin/bash
inputPath=$1
script=$2

for file in $inputPath
do
   python $2 $file
done