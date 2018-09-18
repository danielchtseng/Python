# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 11:11:23 2018

@author: danieltseng
"""

class student:
    def __init__(self, name, age):  #建構子
        self.name = name
        self.age = age
        
    def __str__(self):              #顯示物件本身
        return 'Student: ' + self.name
    
    def info(self):
        print(self.name)
        print(self.age)
    

s1 = student('Daniel',12)           #物件s1建立
s2 = student('Irving',12)           #物件s2建立
s1.info()
print(s1)
print(s2)

