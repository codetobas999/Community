time = float(input("Enter your time [ex 10.00]:"))
if time < 10.00:
    print("Good morning")
elif time < 12.00:
    print("Soon time for lunch")
elif time < 18.00:
    print("Good day")
elif time < 22.00:
    print("Good evening")
else:
    print("Good night")

