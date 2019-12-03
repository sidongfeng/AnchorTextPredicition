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
import numpy as np
import math

def parse_posts():
    savefile = 'table.csv'
    xmlfile = '/Volumes/Macintosh HD/Users/charlie/Documents/Posts.xml'

    # initialize
    if os.path.exists(savefile):
        df = pd.read_csv(savefile)
        try:
            id_start = df.iloc[-1].get(key = 'id') 
        except:
            id_start = 0
        sf = open(savefile,'a')
    else:
        sf = open(savefile,'w')
        sf.write('id,url,description\n')
        id_start = 0
    readfile = open(xmlfile,'r')

    # read backup
    id = 0
    while id < id_start:
        line = readfile.readline()
        try:
            line = ET.fromstring(line)
            id = int(line.get('Id'))
        except:
            pass
        
    print("#"*25)
    print("Start parsing from id", id_start)
    print("#"*25)
    no = 0
    for line in readfile:
        # parse line to id, url, descritption
        try:
            line = ET.fromstring(line)
        except:
            continue
        id = line.get('Id')
        if int(id) % 1000 == 0:
            print(id)
        href = re.findall('<a (.+?)</a>', line.get('Body'))
        for h in href:    
            # parse &#39;
            h = html.unescape(h)    
            if 'class="post-tag"' not in h and 'img src' not in h:
                try:
                    url = re.search('href="(.+?)"', h).group(1)
                except:
                    try:
                        url = re.search('hreF="(.+?)"', h).group(1)
                    except:
                        try:
                            url = re.search('HREF="(.+?)"', h).group(1)
                        except:
                            try:
                                url = re.search('Href="(.+?)"', h).group(1)
                            except:
                                print(h)
                                exit()
                url = url.replace(',','specialcomma')
                description = h.split('">',1)[-1]
                description = re.sub('<.*?>', '', description)
                description = description.replace(',','specialcomma')
                sf.write(id+','+url+','+description+'\n')
        
    readfile.close()
    sf.close()
    
# df =pd.read_csv('table.csv')
# df['description1'] = df['description'].str.lower()
# f = open('table_freq.csv','w')
# f.write(df['description1'].value_counts().to_csv())
# f.close()
# print(df['description1'].value_counts())
# # print(df.iloc[10]['id']) 

# df = pd.read_csv('table_freq.csv', header=None)
# print(df.head(15))

def parse_links():
    df = pd.read_csv('table.csv')
    f = open('table_url.csv','a')
    dfr = pd.DataFrame(columns=['url','ids','descriptions'])
    print('Start parsing')
    for name, group in df.groupby('url'):
        print('$'*10)
        print(name)
        print('$'*10)
        print(group)
        ids = '++++'.join(list(group.id.apply(str)))
        # print(ids)
        descriptions = '++++'.join(list(group.description.apply(str))).replace(',','specialcomma')
        # print(descriptions)
        f.write(name+','+ids+','+descriptions+'\n')
    # uniques = df['url'].unique()
    # for uni in tqdm.tqdm(uniques):
    #     uni_frame = df[df['url'] == uni]
    #     ids = list(uni_frame.id)
    #     descriptions = list(uni_frame.description)
    #     dfr = dfr.append(pd.Series([uni, ids, descriptions],index=['url','ids','descriptions']), ignore_index=True)
    # f = open('table_url.csv','w')
    # f.write(dfr.to_csv(index=False))
    f.close()

def re_parse_links():
    df = pd.read_csv('table_url.csv')
    df = df.dropna()
    total = len(df)
    dfr = pd.DataFrame(columns=df.columns)
    for i, row in df.iterrows():
        print(str(i)+'/'+str(total))
        # print(row['descriptions'])
        ids = row['ids'].split('++++')
        string = row['descriptions'].split('++++')
        dfr = dfr.append(pd.Series([row['url'],ids,string], index=['url','ids','descriptions']),ignore_index=True)
    f = open('table_url2.csv','w')
    f.write(dfr.to_csv(index=False)) 
    f.close()

if __name__ == '__main__': 
    None
    # parse_posts()
    # parse_links()

    #TODO: check 33780156
    # df = pd.read_csv('table_url.csv')
    # print(df[df.isnull().T.any()])  

    xmlfile = '/Volumes/Macintosh HD/Users/charlie/Documents/Posts.xml'
    readfile = open(xmlfile,'r')
    for line in readfile:
        # parse line to id, url, descritption
        try:
            line = ET.fromstring(line)
        except:
            continue
        href = re.findall('<a (.+?)</a>', line.get('Body'))
        for h in href:    
            h = html.unescape(h)    
            if 'class="post-tag"' not in h:
                try:
                    url = re.search('href="(.+?)"', h).group(1)
                except:
                    try:
                        url = re.search('hreF="(.+?)"', h).group(1)
                    except:
                        try:
                            url = re.search('HREF="(.+?)"', h).group(1)
                        except:
                            try:
                                url = re.search('Href="(.+?)"', h).group(1)
                            except:
                                print(h)
                                exit()
                url = url.replace(',','specialcomma')
                if url == '/@jgbneatdesign':
                    description = h.split('">',1)[-1]
                    description = re.sub('<.*?>', '', description)
                    description = description.replace(',','specialcomma')
                    print(description)
                    print(line.get('Body'))
                    break