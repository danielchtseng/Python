# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:39:50 2018

@author: danieltseng
"""

import pandas as pd 


# 資料為 Array

cars = ["BMW", "BENZ", "Toyota", "Nissan", "Lexus"]

select = pd.Series(cars)  
print(select)  
print("#####")  



#資料為 Dictionary

import pandas as pd

dict = {  
    "factory": "Taipei",
    "sensor1": "1",
    "sensor2": "2",
    "sensor3": "3",
    "sensor4": "4",
    "sensor5": "5"
}

select = pd.Series(dict, index = dict.keys()) # 排序與原 dict 相同  
print(select[0])  
print("=====")  
print(select['sensor1'])  
print("=====")  
print(select[[0, 2, 4]])  
print("=====")  
print(select[['factory', 'sensor1', 'sensor3']]) 