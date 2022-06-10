strA = "I "
strB = "am "
strC = "Python "
strD = "GPA "
strE = "= "
strF = 4.0
print(strA + strB + strC + strD + strE + str(strF))

strA = "I"
strB = "am"
strC = "Python"
strD = "GPA"
strE = "="
strF = 4.0
print(strA, strB, strC, strD, strE, strF)

line = "="
print(line*20)
strA = "I"
strB = "am"
strC = "Python"
strD = "GPA"
strE = "="
strF = 4.0
print(strA, strB, strC, strD, strE, strF)
print(line*20)

strA = "I"
strB = "am"
strC = "Python"
strD = "GPA"
strE = "="
strF = 4.0
print(strA, strB, "\\" + strC +"\\", "\n" + strD, strE, strF)

d = 132324.65
print("%-8s%15d" % ("%15d", d))
print("%-8s%15f" % ("%15f", d))
print("%-8s%15.2f" % ("%15.2f", d))
print("%-8s%-15d" % ("%-15d", d))
print("%-8s%-15f" % ("%-15f", d))
print("%-8s%-15.2f" % ("%-15.2f", d))
