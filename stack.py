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

def parse_posts():
    df = pd.DataFrame(columns=['url','description'])
    xmlfile = '/Volumes/Macintosh HD/Users/charlie/Documents/Posts.xml'
    tree = ET.parse(xmlfile) 
    root = tree.getroot()
    items = root.findall('row')
    for item in items:
        # print(item.get('Id'))
        # print(item.get('AcceptedAnswerId'))
        # print(item.get('CreationDate'))
        # print(item.get('Score'))
        # print(item.get('ViewCount'))
        # print(item.get('Body'))
        # print(item.get('OwnerUserId'))
        # print(item.get('LastActivityDate'))
        # print(item.get('Title'))
        # print(item.get('Tags'))
        # print(item.get('AnswerCount'))
        # print(item.get('CommentCount'))
        # print(item.get('FavoriteCount'))
        href = re.findall('<a (.+?)</a>', item.get('Body'))
        for h in href:
            # parse &#39;
            h = html.unescape(h)
            # if  in h:
            #     print(item.get('Body'))
            #     return
            if 'class="post-tag"' not in h and 'img src' not in h:
                url = re.search('href="(.+?)">', h).group(1)
                description = h.split('">',1)[-1]
                description = re.sub('<.*?>', '', description)
                print(description)
                new_frame = pd.Series([url,description],index=['url','description'])
                df = df.append(new_frame,ignore_index=True)
    print(Counter(list(df['description'])).most_common(10))

parse_posts()


# posts, users, comments, history

# xmlfile = '/Users/mac/Downloads/3dprinting.meta.stackexchange.com/Comments.xml'
# tree = ET.parse(xmlfile) 
# root = tree.getroot()
# items = root.findall('row')

if __name__ == '__main__': 
    None