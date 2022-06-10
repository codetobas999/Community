N = int(input("จำนวนนิสิต >>> "))
avg = 0
total = 0
for count in range(1, (N + 1)):
    score = float(input("คะแนนสอบของนิสิตคนที่ " +
                        str(count) + "  >>> "))
    total += score
avg = total / N
print("คะแนนเฉลี่ยเท่ากับ", avg)

