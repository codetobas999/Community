def menu():
    print("*" *25)
    print("* Registration system   *")
    print("*" *25)
    print("* 1. Insert data        *")
    print("* 2. Delete data          *")
    print("* 3. Update data        *")
    print("* 4. Show data        *")
    print("* 0. Exit program       *")
    print("*" *25)
menu()
choice = int(input("Enter your choice ="))
while choice != 0:
    if choice == 1:
        print("call insert data function")
    elif choice == 2:
        print("call delete data function")
    elif choice == 3:
        print("call update data function")
    elif choice == 4:
        print("call show data function")
    else:
        print("Your choice was wrong!, plase choose a new one [1-4]")
    menu()
    choice = int(input("Enter your choice ="))
else:
    print("Program exit!")

    
