mydata1 = ["C", "JAVA", "PYTHON"]
print(mydata1[0], end=" ")
print(mydata1[1], end=" ")
print(mydata1[2], end="\n")
print(mydata1[0], end=";")
print(mydata1[1], end=":")
print(mydata1[2], end="\n")
mydata2 = ["BANGKOK", "CHIANGMAI", "SONGKHLA"]
print(mydata2[0], mydata2[1], mydata2[2], end="\n", sep="-")
print("see u!")

print("="*30)

x = "Python"
y = "Programming"
print("{:s}".format(x))
print("{:s} {:s}".format(x, y))
print("{1:s} by {0:s}".format(x, y))
print("{:*<10s}  {:*^15s}".format(x, y))
a = 1070.999
b = 6.97
print("{:*>10.1f} {:*>10.2f}".format(a, b))
print("{:10.1f} {:*^10.2f}".format(a, b))
print("="*30)
