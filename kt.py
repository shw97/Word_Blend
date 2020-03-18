#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:18:32 2019

@author: shwetha
"""
from pyjarowinkler import distance

print(distance.get_jaro_distance("brunch", "break", winkler=True, scaling=0.1))
import csv
import pandas
word_list_blend = []

word_list = []
with open('/Users/shwetha/Desktop/Desktop/2019S2-COMP90049_proj1-data/candidates.txt', 'r') as f:
    reader = csv.reader(f, dialect='excel')
    word_list_blend = list(reader)

#blend = []
columns = ['blend', 'word1','word2']
#with open('/Users/shwetha/Desktop/Desktop/2019S2-COMP90049_proj1-data/blends_org.txt', 'r') as f:
#    reader = csv.reader(f, dialect='excel')
#    blend = pandas.DataFrame(reader,columns = columns)
blend = pandas.read_table('/Users/shwetha/Desktop/Desktop/2019S2-COMP90049_proj1-data/blends_org.txt', delim_whitespace=True, names=('blend', 'word1', 'word2'))
print(blend)
#    word_list_boolean = list(reader)
#    word_list_boolean_end = list(reader)
    #for row in reader:
#    i = 0
#    while i < len(reader):
#        print(i)
#        word_list_blend[i] = reader[i]
#        i = i + 1
        
with open('/Users/shwetha/Desktop/Desktop/2019S2-COMP90049_proj1-data/dict.txt', 'r') as f:
    reader = csv.reader(f, dialect='excel')
    word_list = list(reader)
with open('/Users/shwetha/Desktop/Desktop/2019S2-COMP90049_proj1-data/dict.txt', 'r') as f:
    reader = csv.reader(f, dialect='excel')
    word_list_boolean = list(reader)
with open('/Users/shwetha/Desktop/Desktop/2019S2-COMP90049_proj1-data/dict.txt', 'r') as f:
    reader = csv.reader(f, dialect='excel')
    word_list_boolean_end = list(reader)
    print("lengths",len(word_list),len(word_list_boolean))
    #for row in reader:
#    i = 0
#    while i < len(reader):
#        print(i)
#        word_list[i] = reader[i]
#        i = i + 1
def similarity_comp(word,begin,threshold,end,each):   
    while each < len(word_list):
        demo = word_list[each]
        demo = str(demo)
#        print(type(demo))
        if(demo.startswith(word[0:threshold-1])):
#        print("In the loop")
            word_list_boolean[each] = 1
        else:
            word_list_boolean[each] = 0
        each += 1
    each1 = 0 

    while each1 < len(word_list):   
        demo = word_list[each1]
        demo = str(demo)
#    print(type(demo))
        if(demo.endswith(word[threshold:end+1])):
            word_list_boolean_end[each1] = 1
        else:
            word_list_boolean_end[each1] = 0
        each1 += 1
    each = 0  
    blend = 0     
    while each < len(word_list):
#    print("prefix values:")
#    
#    print( word_list_boolean[each])
#    print("suffix values:")
#    print( word_list_boolean_end[each])
        if(word_list_boolean[each] == 1):
            print(word_list[each])
            blend = blend + 1
            break
        each += 1
    each = 0
    while each < len(word_list):
        if(word_list_boolean_end[each] == 1):
            print(word_list[each])
            blend = blend + 1
            break
        each += 1
        
    if(blend == 2):
        print('Word is blend')
i = 0   
####Reqd Code     
while i < len(word_list_blend):        
    word = word_list_blend[i]#'brunch'
    word = str(word)
#word_list = ['breakfast','break','bone','yell','crunch','lunch']
#word_list_boolean = ['breakfast','break','bone','yell','crunch','lunch']
#word_list_boolean_end = ['breakfast','break','bone','yell','crunch','lunch']
    threshold = int(len(word)/2)
#print(type(threshold))
    begin = 0
    end = len(word)
    each = 0
    similarity_comp(word,begin,threshold,end,each)
    i = i + 1
####Reqd code end
#print('demo:')
##print(word_list[0].startswith('br',0,3))
#print(word_list[0].endswith(word[3:len(word)+1]))

    
#f = open("sample_txt1.txt", "r")
#with open('data1.json', 'w') as outfile:
#    json.dump(trial, outfile)
#file1 = open("sample_txt1.txt", "r")
#print(file1.readlines())
#import csv
#with open('sample_txt1.txt', 'r') as f:
#    reader = csv.reader(f, dialect='excel', delimiter=' ')
#    for row in reader:
#        print(row)
#import csv
#
#with open('sample_txt1.txt', mode='r') as csv_file:
#    csv_reader = csv.DictReader(csv_file)
#print(csv_reader)
# 
def f1measure(precision,recal):
    num = 2 * precision * recal
    deno = precision + recal
    print(num/deno)

def recal(word_list,blend):
    Totaltpfp_attempted = len(word_list)
#    print("deno=",Totaltpfp_attempted)
    blend_comp_len = len(blend['blend'])
#    print("blendfile=",blend_comp_len)
    fp = Totaltpfp_attempted - blend_comp_len
    tp = blend_comp_len
#    print("tp=",tp)
    recal = tp / blend_comp_len
    print(recal)
    return recal
    
def precision_cal(word_list,blend):
    Totaltpfp_attempted = len(word_list)
#    print("deno=",Totaltpfp_attempted)
    blend_comp_len = len(blend['blend'])
#    print("blendfile=",blend_comp_len)
    fp = Totaltpfp_attempted - blend_comp_len
    tp = blend_comp_len
#    print("tp=",tp)
    precision = tp / Totaltpfp_attempted
    print(precision)
    return precision
    
def accuracy_cal(word_list,blend):
    Totaltpfp = len(word_list)
#    print("deno=",Totaltpfp)
    blend_comp_len = len(blend['blend'])
#    print("blendfile=",blend_comp_len)
    fp = Totaltpfp - blend_comp_len
    tp = blend_comp_len
#    print("tp=",tp)
    precision = tp / Totaltpfp
    print(precision)
    
print('Precision Value is:')
precision = precision_cal(word_list,blend)  
print('Accuracy Value is:')
accuracy_cal(word_list,blend)      
print('Recall Value is:')
recal = recal(word_list,blend)  
print('F1 Measure Value is:')
f1measure(precision,recal)  

######OUTPUT VALUE:
#[183 rows x 3 columns]
#lengths 34856 34856
#Precision Value is:
#0.00525017213679137
#Accuracy Value is:
#0.00525017213679137
#Recall Value is:
#1.0
#F1 Measure Value is:
#0.010445503581723222
###########3