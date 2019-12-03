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
xmlfile = '/Volumes/Macintosh HD/Users/charlie/Documents/Posts.xml'
readfile = open(xmlfile,'r')

creation_range = {'min':datetime.datetime.strptime('2020-12-31T12:59:59.001','%Y-%m-%dT%H:%M:%S.%f'), 'max':datetime.datetime.strptime('0001-01-01T01:01:01.001','%Y-%m-%dT%H:%M:%S.%f')}
score_range = {'min':float('Inf'), 'max':-float('Inf')}
view_range = {'min':float('Inf'), 'max':-float('Inf')}
last_range = {'min':datetime.datetime.strptime('2020-12-31T12:59:59.001','%Y-%m-%dT%H:%M:%S.%f'), 'max':datetime.datetime.strptime('0001-01-01T01:01:01.001','%Y-%m-%dT%H:%M:%S.%f')}
answer_range = {'min':float('Inf'), 'max':-float('Inf')}
comment_range = {'min':float('Inf'), 'max':-float('Inf')}
favourite_range = {'min':float('Inf'), 'max':-float('Inf')}

for line in readfile:
    try:
        line = ET.fromstring(line)
    except:
        continue
    id = line.get('Id')
    if int(id) % 1000 == 10:
        print(id)
    creation = datetime.datetime.strptime(line.get('CreationDate'),'%Y-%m-%dT%H:%M:%S.%f')
    if creation > creation_range['max']:
        creation_range['max'] = creation
    if creation < creation_range['min']:
        creation_range['min'] = creation

    try:
        score = int(line.get('Score'))
        if score > score_range['max']:
            score_range['max'] = score
        if score < score_range['min']:
            score_range['min'] = score
    except:
        pass

    try:
        view = int(line.get('ViewCount'))
        if view > view_range['max']:
            view_range['max'] = view
        if view < view_range['min']:
            view_range['min'] = view
    except:
        pass

    try:
        last = datetime.datetime.strptime(line.get('LastEditDate'),'%Y-%m-%dT%H:%M:%S.%f')
        if last > last_range['max']:
            last_range['max'] = last
        if last < last_range['min']:
            last_range['min'] = last
    except:
        pass

    try:
        answer = int(line.get('AnswerCount'))
        if answer > answer_range['max']:
            answer_range['max'] = answer
        if answer < answer_range['min']:
            answer_range['min'] = answer
    except:
        pass

    try:
        comment = int(line.get('CommentCount'))
        if comment > comment_range['max']:
            comment_range['max'] = comment
        if comment < comment_range['min']:
            comment_range['min'] = comment
    except:
        pass

    try:
        favourite = int(line.get('FavoriteCount'))
        if favourite > favourite_range['max']:
            favourite_range['max'] = favourite
        if favourite < favourite_range['min']:
            favourite_range['min'] = favourite
    except:
        pass

print(answer_range)
print(comment_range)
print(favourite_range)


if __name__ == '__main__': 
    None
    creation_range = {'min': datetime.datetime(2008, 7, 31, 21, 42, 52, 667000), 'max': datetime.datetime(2019, 9, 1, 5, 24, 14, 550000)}
    score_range = {'min': -166, 'max': 30552}
    view_range = {'min': 2, 'max': 8083391}
    last_range = {'min': datetime.datetime(2008, 8, 1, 13, 16, 49, 127000), 'max': datetime.datetime(2019, 9, 1, 5, 23, 41, 743000)}
    answer_range = {'min': 0, 'max': 518}
    comment_range = {'min': 0, 'max': 157}
    favourite_range = {'min': 0, 'max': 10635}
    # print(last_range['min'])
    # print(last_range['max'])