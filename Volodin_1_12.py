amount = int(input())

rubles = int(input())
pennies = int(input())

priceR = rubles * amount
priceP = pennies * amount
finalPriceP = priceP % 100
finalPriceR = priceR + (priceP // 100)

print(finalPriceR, ',', finalPriceP, sep=(''))
