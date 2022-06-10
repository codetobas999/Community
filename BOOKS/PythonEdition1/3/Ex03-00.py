A = 9 > 5
B = 9 - 5 > 9 + 5
C = True
D = False
print(A, B, C, D)

ans = None
x = 3
y = 0
if y != 0:
    ans = x/y
print(ans)

strA = "3020158"
strB = '3020158'
strC = '"Monday"'
strD = "'Jan'"
strE = "A & " \
            "B"
strF = "A"
noF = ord(strF)
print(strA, strB, strC, strD, strE, strF, noF)

listA = ["Anna", 20, "Bangkok", "Aree", 22, "Chiangmai"]
print("list A =", listA)
listA.append("Adam")
print("list A =", listA)
print(listA[0])
print(listA[1])
print(listA[2])
print(listA[3])
print(listA[4])
print(listA[5])

tupleA = ("Anna", 20, "Bangkok", "Aree", 22, "Chiangmai")
tupleB = "Anna", 20, "Bangkok", "Aree", 22, "Chiangmai"
print("tuple A =", tupleA)
print("tuple B =", tupleB)
print(tupleA[0])
print(tupleA[1])
print(tupleA[2])
print(tupleB[3])
print(tupleB[4])
print(tupleB[5])

setA = {"Anna", 20, "Bangkok", "Aree", 22, "Chiangmai", 22}
print("set A =", setA)
setA.add("Aree")
print("set A =", setA)

scores = {'Anna': 20.6, 'Meena': 22.1, 'Wanna': 23.0}
scores['Weena'] = 21.7
print(scores['Weena'])
print(scores['Meena'])
print(scores['Wanna'])
print(scores['Anna'])

a = 5
print(type(a))
b = 5.0
print(type(b))
c = [1, 2, 3]
print(type(c))
d = (1, 2, 3)
print(type(d))
e = {1, 2, 3}
print(type(e))
f = {1: "one", 2: "two", 3: "three"}
print(type(f))
g = float
print(type(g))
h = len
print(type(h))

print("A"+"&"+"B")
print("A","&","B")

print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2)
print(3 % 2)
print(3 ** 2)

print(9 + 2)
print(9 - 2)
print(9 * 2)
print(9 / 2)
print(9 // 2)
print(9 % 2)
print(9 ** 2)

print(9 == 2)
print(9 != 2)
print(9 > 2)
print(9 >= 2)
print(9 < 2)
print(9 <= 2)

print((9>=2) and (9!=2))
print((9>=2) or (9!=2))
print(not  (9!=2))

A = 65
print("a=" ,  bin(A))
B = 33
print("b=" ,  bin(B))

print("A=" , bin(A & B))
print("A=" , bin(A | B))
print("A=" , bin(A ^ B))
print("B=" , bin(B << 2))





strA = ("Bangkok", 200, "Chiangmai", 200)
print(strA)
strA = ["Bangkok", 200, "Chiangmai", 200]
print(strA)
strA = []
print(strA)
strA = {"Bangkok", 200, "Chiangmai", 200}
print(strA)
str1 = "A"+"&"+"B"
str2 = "A","&","B"
print(str1)
print(str2)
print("A"+"&"+"B")
print("A","&","B")
str1 = "A"
print(str1)
Asc1 = (ord(str1))
print(Asc1)
print(chr(Asc1))
a = hex(10)
print(a)
a = oct(10)
print(a)
a = bin(10)
print(a)
A = 7.5
A //= 3
print(A)
A -= 2
print(A)
A *= 8
print(A)
A /= 4
print(A)
A //= 5
print(A)
A %= 3
print(A)
A = 'A'
B = 't'
C = -5.5
D = -2.5
X = 256
Y = 8
print((B <= A) or ((D-C) > 0))
print((X >> 2) | (Y << 1))
