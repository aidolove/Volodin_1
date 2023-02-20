# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 12:21:22 2023

@author: 309-uk2
"""

N = int(input())

a = N // 100
b = N // 10 % 10 
c = N % 10

print(a + b + c)