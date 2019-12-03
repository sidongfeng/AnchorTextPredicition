# -*- coding: utf-8 -*-
"""
Created on Fri Feb 3 12:40:12 2019

@author: Sidong Feng
"""
import os
import argparse
import urllib.request
from time import perf_counter 
from selenium import webdriver

import pandas as pd
import xml.etree.ElementTree as ET
import io
import re
import html
from collections import Counter
import random
import datetime
from lxml import etree

# df = pd.read_csv('table.csv')
# df1 = pd.read_csv('output(1).csv',header=None)
# df_r = pd.DataFrame(columns=['id','url','anchor'])
# for i, row in df1.iterrows():
#     if i%50==0:
#         print(i)
#     frame = df.loc[(df['url'] == row[1]) & (df['description'] == row[2])]
#     if len(frame) != 1:
#         print(row)
#     else:
#         df_r = df_r.append(frame,ignore_index=True)

# f = open('test.csv','w')
# f.write(df_r.to_csv(index=False))
# f.close()


###### Diversity #######
# xmlfile = '/Volumes/Macintosh HD/Users/charlie/Documents/PostHistory.xml'
# readfile = open(xmlfile,'r')

# no = 0

# for line in readfile:
#     try:
#         line = ET.fromstring(line)
#     except:
#         continue
#     id = line.get('Id')
#     if int(id) % 1000 == 0:
#         print(id)
#     hid = line.get('PostHistoryTypeId')
#     if hid == '2' or hid == '5' or hid == '8':
#         no += 1
    
# print(no)
# 72833122


###############################################################
###############################################################
# file = "/Volumes/Macintosh HD/Users/charlie/Documents/PostHistory.xml"
# input = open(file, 'r', encoding='utf-8')
# line = input.readline()
# output = open("no.csv","a",encoding='utf-8')
# output.write("id,postid\n")
# output.close()

# print('Start')
# # post_dict = {}
# no = 0
# while "</posthistory>" not in line:
#     if "<row" in line:
#         context = etree.fromstring(line)
#         text = context.xpath("//@Text")
#         if len(text) != 0:
#             hID = context.xpath("//@PostHistoryTypeId")[0]
#             id = context.xpath("//@Id")[0]
#             postID = context.xpath("//@PostId")[0]

#             if hID == "2" or hID == "5" or hID == "8":
#                 output = open("no.csv","a",encoding='utf-8')
#                 output.write(id+','+postID+'\n')
#                 output.close()
#                 no += 1
#                 if no % 10000 == 0 :
#                     print(no)
#     line = input.readline()
# input.close()

# df = pd.read_csv('no.csv')
# df = df.drop_duplicates(subset=['postid'], keep='last')
# print(df)



if __name__ == '__main__': 
    None