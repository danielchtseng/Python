# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 14:01:47 2018

@author: danieltseng
"""


from datetime import datetime
# *** get ***

# Python Method
import requests
url = "https://www.thsrc.com.tw/index.html"
response1 = requests.get(url)
print(response1.text)

# urllib Method
import urllib.request
from bs4 import BeautifulSoup as bs
response2 = urllib.request.urlopen(url)
html_cont = response2.read()
soup = bs(html_cont,)

# Pandas Method (Series & Dataframe)
import pandas
dfs = pandas.read_html(url) 



# *** post ***
dt = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
date = datetime.now().strftime("%Y/%m/%d")
time = datetime.now().strftime("%H:%M:%S")
print(dt)
print(date)
print(time)

payload = {     #Dictionary
   'StartStation': '977abb69-413a-4ccf-a109-0272c24fd490',
   'EndStation': '3301e395-46b8-47aa-aa37-139e15708779',
   #'SearchDate': '2018/08/23',
   'SearchDate': "date",
   'SearchTime': '18:00',
   'SearchWay': 'DepartureInMandarin'     
        }

url2 = "https://www.thsrc.com.tw/tw/TimeTable/SearchResult"
response2 = requests.post(url2,data=payload)
print(response2.text)



