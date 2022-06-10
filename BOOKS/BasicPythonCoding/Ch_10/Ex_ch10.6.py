num = int(input("Enter the number of students:"))
dic = {}
while num > 0:
    idx = input("Enter your ID:")
    name = input("Enter your name:")
    age = input("Enter your age:")
    dic[idx] = [name, age]
    num = num - 1
#print all student members
print(dic)
#print each student member
for data in dic:
    print(dic[data])
