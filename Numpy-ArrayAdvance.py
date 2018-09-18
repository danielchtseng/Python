# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 10:54:41 2018

@author: danieltseng
"""
import numpy as np

er = 30.0
us = [10,20,30,40,50]
print(type(us))          # list
print(us)
#us = us*er
#print(us)

print("#####")
prices = np.array(us)
print(type(prices))     # array
print(prices)

prices = prices*er
print(prices)
