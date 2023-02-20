# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 12:33:34 2023

@author: 309-uk2
"""

N = int(input())
hours = N // 60 - ((N // 60) // 24) * 24
minutes = N % 60

print(hours, ':', minutes, sep='')