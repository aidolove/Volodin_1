x = int(input())
hours = x // 60 - ((x // 60) // 24) * 24
minutes = x % 60

print(hours, ':', minutes, sep='')
