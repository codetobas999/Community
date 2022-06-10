n = int(input("Enter number of people: "))
m = n - 3 # (n - r)!
x, y = 1, 1
while n > 0: #หาค่า n!
    x = x * n #หาค่า n*(n-1)*(n-2)*(n-3)*…*1
    n = n - 1
while m > 0: #หาค่า (n – r)!
    y = y * m
    m = m - 1
print("P = ", x/y)
