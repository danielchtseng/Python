# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:25:02 2018

@author: danieltseng
"""
import requests
import pandas as pd
import time


# pandas read_html()
time.sleep(3)   # evading url denied
dfs = pandas.read_html(url)
extab = dfs[0]
