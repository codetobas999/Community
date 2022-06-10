x = int(input("Enter number of Durian (kilo) = "))
y = float(input("Enter purchase price (baht) = "))
z = float(input("Enter sale price (baht) = "))
Cost = x * y
Total = x * z
Profit = (Total * 100) / Cost
print("Total profit = %.2f" %(Profit), "%")
