
# coding: utf-8
"""
@created by: shwetha Srinivasan
"""

from similarity.ngram import NGram
from pathlib import Path
import csv
import pandas as pd
from sklearn import metrics


cpath = open("/Users/shwetha/Desktop/Desktop/2019S2-COMP90049_proj1-data/candidates.txt","r")
dpath = open("/Users/shwetha/Desktop/Desktop/2019S2-COMP90049_proj1-data/dict.txt","r")
bpath = open("/Users/shwetha/Desktop/Desktop/2019S2-COMP90049_proj1-data/blends_org.txt","r")

wordscheck=[]
twogram=NGram(2)

candidates= csv.reader(cpath,dialect = "excel")
dictionary=csv.reader(dpath,dialect = "excel")

blends=pd.read_table(bpath,names=("blends","w1","w2"))


blends.head()

blends.tail()

blends.head(20)

dictwords=list(dictionary)

blendwords=list(blends)

candiwords=list(candidates)

#wordscheck = dictwords #copy list

lc = (len(candiwords))

ld = (len(dictwords))

print ("length of candidates.txt=",lc, "\n")
print ("length of dict.txt=",ld, "\n")

cfinal = []

for c in candiwords:
    for d in dictwords:
        if c == d:
            cfinal.append(c)

for c in cfinal:
    m = int(len(c/2))
    c1=c[:m]
    c2=c[m:]

dictmatch1=0
dictmatch2=0

b1 = ""
b2 = ""
twogram = NGram(2)


for d in dictwords:
    d1 = dictwords[:m]
    distance = twogram.distance(c1,d1)
    if distance > dictmatch1:
       dictmatch1 = distance
       b1 = dictmatch1

for dictwords in dictionary:
    d2 = dictwords[m:]
    distance = twogram.distance(c2,d2)
    if distance > dictmatch1:
       dictmatch2 = distance
       b2 = dictmatch2

print ("candidate words","=",b1," + ",b2,"\t")

final = b1+b2

def f1measure(precision,recall):
    num = 2 * precision * recall
    final = precision + recall
    print(num/final)

def recall(final,blends):
    Totaltpfp_attempted = len(final)
    blend_comp_len = len(blends['blends'])
    fp = Totaltpfp_attempted - blend_comp_len
    tp = blend_comp_len
    recall = tp / blend_comp_len
    print(recall)
    return recall

def precision_cal(final,blends):
    Totaltpfp_attempted = len(final)
    blend_comp_len = len(blends['blends'])
    fp = Totaltpfp_attempted - blend_comp_len
    tp = blend_comp_len
    precision = tp / Totaltpfp_attempted
    print(precision)
    return precision

def accuracy_cal(final,blends):
    Totaltpfp = len(final)
    blend_comp_len = len(blends['blends'])
    fp = Totaltpfp - blend_comp_len
    tp = blend_comp_len
    accuracy = tp / Totaltpfp
    print(accuracy)

print('Precision Value is:')
precision = precision_cal(final,blends)  
print('Accuracy Value is:')
accuracy_cal(final,blends)      
print('Recall Value is:')
recal = recall(final,blends)  
print('F1 Measure Value is:')
f1measure(precision,recall) 

