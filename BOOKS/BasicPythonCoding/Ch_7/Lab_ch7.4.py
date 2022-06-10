a = float(input("Enter base length = "))
b = float(input("Enter isosceles length = "))
Area = a/4 * ((a * (b ** 2)) - (a ** 2)) ** (1/2)
print("Area of isosceles triangle = %.2f" %(Area))
