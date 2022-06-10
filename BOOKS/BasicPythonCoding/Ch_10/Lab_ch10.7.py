n = int(input("Enter integer number: "))
Sum = 0
for i in range(2, n + 1):
    if i % 2 != 0:
        continue
    else:
        Sum = Sum + i
print("Sum  = ", Sum)
        
