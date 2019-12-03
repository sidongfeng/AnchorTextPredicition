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

savefile = 'Posts.csv'
f = open(savefile,'a')
# f.write('Id,CreationDate,Score,Body,LastEditDate\n')
# df = pd.DataFrame(columns=['Id','CreationDate','Score','Body','LastEditDate'])
xmlfile = '/Volumes/Macintosh HD/Users/charlie/Documents/Posts.xml'
readfile = open(xmlfile,'r')
for line in readfile:
    try:
        line = ET.fromstring(line)
    except:
        continue
    id = line.get('Id')
    if int(id) % 1000 == 0:
        print(id)
    CreationDate = str(line.get('CreationDate'))
    Score = str(line.get('Score'))
    Body = str(line.get('Body'))
    LastEditDate = str(line.get('LastEditDate'))
    f.write(id+','+CreationDate+','+Score+','+Body+','+LastEditDate+'\n')
    # df = df.append(pd.Series([id,CreationDate,Score,Body,LastEditDate], index=['Id','CreationDate','Score','Body','LastEditDate']),ignore_index=True)
# f = open(savefile,'w')
# f.write(df.to_csv(index=False))
f.close()



if __name__ == '__main__': 
    None