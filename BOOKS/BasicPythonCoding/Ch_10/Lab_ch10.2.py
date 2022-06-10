n = int(input("Enter your number: "))
x, y = 1, 1
while n > 0:
    x = x * n
    if n == 1:
        break
    else:
        y = y * (n - 1)
    n = n - 1
print("Factorial = ", x/y)
