# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:25:02 2018

@author: danieltseng
"""
import requests
import pandas as pd
import time

url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
# python request.get
time.sleep(3)   # evading url denied
res = requests.get(url)
print (res.text)

# pandas read_html()

time.sleep(3)   # evading url denied
dfs = pd.read_html(url)
extab = dfs[0]
