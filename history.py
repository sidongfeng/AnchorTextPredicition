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


savefile = 'table12.csv'
xmlfile = '/Volumes/Macintosh HD/Users/charlie/Documents/PostHistory.xml'
readfile = open(xmlfile,'r')
print("#"*25)
# print("Start parsing from id", id_start)
print("#"*25)
# print(readfile.readline())
# print(readfile.readline())
# print(readfile.readline())
for line in readfile:
    # parse line to id, url, descritption
    try:
        line = ET.fromstring(line)
    except:
        continue
    if line.get('PostId') == '14':
        string = line.get('Text')
        print('#'*20)
        print(line.get('Text'))
        bib = [x.split(']: ')[1] for x in string.split('\n') if x.startswith('  [')]
        bib = [x[:-1] if '\r' in x else x for x in bib]
        print('Bib:', bib)
        index = re.findall('\[.*?\]',string)[:-len(bib)]
        print('Index', index)

        print('#'*20)



# string = "I am aware in dot net there are three timer types (see [http://msdn.microsoft.com/en-us/magazine/cc164015.aspx][1]). I have chosen a the threaded timer as the other types can drift if the main thread is busy and I need this to be reliable.The way this timer works in the control of the timer is put on another thread so it can always tick along with the work begin completed on the parent thread when it is not busy.The issue I have is that with this timer in a console application is that while the timer is ticking along on another thread the main thread is not doing anything so the app closes.I tried adding a while true loop but then the main thread is too busy when the timer does go off.Any ideas welcome.[1]: http://msdn.microsoft.com/en-us/magazine/cc164015.aspx"
# m = re.findall('\[.*?\]',string)
# print(m)


# df =pd.read_csv('table.csv')
# print(len(df))
# print(Counter(list(df['description'])).most_common(10))

if __name__ == '__main__': 
    None
    # parse_posts()