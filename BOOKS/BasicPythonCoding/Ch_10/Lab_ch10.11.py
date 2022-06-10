a = [[4, 1, 7],
     [2, 4, 8],
     [3, 7, 1]]

b = [[6, 8, 1],
     [9, 7, 5],
     [2, 4, 3]]

c = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j] += a[i][k] * b[k][j]

for r in c:
 print(r)
