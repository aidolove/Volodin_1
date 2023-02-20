N = int(input())
hours = N // 60 - ((N // 60) // 24) * 24
minutes = N % 60

print(hours, ':', minutes, sep='')
