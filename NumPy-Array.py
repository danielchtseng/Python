# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 16:45:36 2018

@author: danieltseng
"""

# 引入 numpy 模組
import numpy as np

np1 = np.array([1, 2, 3])

# 顯示相關資訊
print(type(np1))            # Prints "<class 'numpy.ndarray'>"
print(np1.ndim)
print(np1.shape) 
print(np1.dtype)
print(np1.ndim, np1.shape, np1.dtype) # 1 (3,) int64 => 一維陣列, 三個元素, 資料型別


np2 = np.array([[1,2,3],[4,5,6]]) 
print(np2[0,0], np2[1,2])


# 
np3 = np.array([1, 2, 3, 4, 5, 6])
print(np3.ndim, np3.shape) # 1 (6,  )
np3 = np3.reshape([2, 3])
print(np3.ndim, np3.shape) # 2 (2, 3) 


np4 = np.zeros((2,2))
print(np4)


np5 = np.ones((2,2))
print(np5)


np6 = np.full((2,2),7)
print(np6)




