# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 14:01:47 2018

@author: danieltseng
"""

import requests
from bs4 import BeautifulSoup 

url = "https://www.thsrc.com.tw/tw/TimeTable/SearchResult"

payload = {     #Dictionary
   'StartStation': '977abb69-413a-4ccf-a109-0272c24fd490',
   'EndStation': '3301e395-46b8-47aa-aa37-139e15708779',
   'SearchDate': '2018/09/06',
   'SearchTime': '18:00',
   'SearchWay': 'DepartureInMandarin'     
}

response = requests.post(url,data=payload)
html = response.text
soup = BeautifulSoup(html,'html.parser')
#print(soup)
print(soup.prettify())










