R = int(input("ค่าโดยสารต่อคน >>> "))
N = int(input("จำนวนคน >>> "))
print("รายการแสดงราคาค่าโดยสาร")
for count in range(1, (N + 1)):
    total = count * R
    print(R, "*", count, "=", total)

