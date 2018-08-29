# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:52:43 2018

Pandas: Flexible and powerful data analysis / manipulation library for Python, 
providing labeled data structures similar to R data.frame objects, 
statistical functions, and much more.

@author: danieltseng
"""

# 讀入 excel 試算表

import pandas as pd

xlsx_file = "D:\Language\Python\Daniel\extab.xlsx"
extab = pd.read_excel(xlsx_file)

"""
df.shape：這個 DataFrame 有幾列有幾欄
df.columns：這個 DataFrame 的變數資訊
df.index：這個 DataFrame 的列索引資訊
df.info()：關於 DataFrame 的詳細資訊
df.describe()：關於 DataFrame 各數值變數的描述統計
"""

print(extab.head()) # show only first five elements of the DataFrame
print("----------------------------------------")
print(extab.tail()) # show only last five elements of the DataFrame
print("----------------------------------------")
#print(type(extab))
#print(extab.shape)
#print(extab.index)
#print(extab.columns)
#print(extab.describe())


