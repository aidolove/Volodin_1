# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 12:56:31 2023

@author: 309-uk2
"""

amount = int(input())

rubles = int(input())
pennies = int(input())

priceR = rubles * amount
priceP = pennies * amount
finalPriceP = priceP % 100
finalPriceR = priceR + (priceP // 100)

print(finalPriceR, ',', finalPriceP, sep=(''))