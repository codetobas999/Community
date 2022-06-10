lst = [23.5, 12.8, 9.75, 18.7, 32.3, 19.0, 26.4, 10.15]
sum = 0
for i in lst:
    sum = sum + i
    n = len(lst)
result = sum / n
print("Average = %.2f" %result)
