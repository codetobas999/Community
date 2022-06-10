def Sum(data):
    sum = 0
    for i in data:
        sum = sum + i
    return sum

lst = [2, 5, 1, 6, 7, 9, 10, 4]
print("Sum of lst =", Sum(lst))
