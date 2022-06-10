n = int(input("Enter n = "))
N = n
SUM = 0
while n > 0:
    SUM = SUM + n
    n = n - 1
result = SUM / N
print("x = ", result)
