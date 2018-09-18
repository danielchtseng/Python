# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:25:02 2018

@author: danieltseng
"""
import requests
import pandas
import time


# request get()
url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
time.sleep(3)   # evading url denied
res = requests.get(url)
print(res.text)