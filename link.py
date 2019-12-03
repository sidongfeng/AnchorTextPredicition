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
import tqdm
import datetime
import operator

def parse_link():
    savefile = 'linkage.csv'
    postfile = '/Volumes/Macintosh HD/Users/charlie/Documents/Posts.xml'
    historyfile = '/Volumes/Macintosh HD/Users/charlie/Documents/PostHistory.xml'
    postreadfile = open(postfile,'r')
    historyreadfile = open(historyfile,'r')
    # initialize
    if os.path.exists(savefile):
        df = pd.read_csv(savefile)
        try:
            id_start = int(df.iloc[-1].get(key = 'id'))
        except:
            id_start = 0
        sf = open(savefile,'a')
    else:
        sf = open(savefile,'w')
        sf.write('id,text\n')
        id_start = 0
    # read backup
    id = 0
    while id < id_start:
        line = postreadfile.readline()
        try:
            line = ET.fromstring(line)
            id = int(line.get('Id'))
        except:
            pass
        
    print("#"*25)
    print("Start parsing from id", id_start)
    print("#"*25)
    no = 0
    for postline in postreadfile:
        # parse line to id, text
        try:
            postline = ET.fromstring(postline)
        except:
            continue
        id = postline.get('Id')
        if int(id) % 1000 == 0:
            print(id)
        href = re.findall('<a (.+?)</a>', postline.get('Body'))
        if len(href)>0:
            currentstring = postline.get('Body').replace(',','specialcomma')
            strings = []
            for postline in historyreadfile:
                try:
                    postline = ET.fromstring(postline)
                except:
                    continue
                if postline.get('PostId') == id:
                    # Strings: <text, date>
                    strings.append((postline.get('Text'),datetime.datetime.strptime(postline.get('CreationDate'),'%Y-%m-%dT%H:%M:%S.%f'), postline.get('Id')))
            # TODO: sort strings
            strings.sort(key=operator.itemgetter(1))
            print(strings)
            print('-'*50)
            break
            # sf.write(id+','+currentstring+'\n')
        
    postreadfile.close()
    historyreadfile.close()
    sf.close()

# historyfile = '/Volumes/Macintosh HD/Users/charlie/Documents/PostHistory.xml'
# tree = ET.parse(historyfile) 
df = pd.read_csv('table.csv', chunksize=20000)
for chunk in df:   
    print(chunk.shape)

if __name__ == '__main__': 
    None
    # parse_link()