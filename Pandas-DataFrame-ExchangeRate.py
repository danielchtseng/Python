# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:25:02 2018

@author: danieltseng
"""
import requests
import pandas

url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
res = requests.get(url)
#print (res1.text)
dfs = pandas.read_html(url)
extab = dfs[0]
extab = extab.iloc[:,0:5]
extab.columns = [u'幣別',u'現金匯率-本行買入',u'現金匯率-本行賣出',u'即期匯率-本行買入',u'即期匯率-本行賣出']
extab[u'幣別'] = extab[u'幣別'].str.extract('\((\w+)\)')

extab.to_excel('extab.xlsx','sheet1') # save DFS into excel file
extab.to_excel('extab.xlsx','sheet2')