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
def GPA(lst):
    sum = 0.0
    unit_count = 0
    for i in lst:
        grade = 0
        if i >= 80:
            grade = 4.0
        elif i >= 75:
            grade = 3.5
        elif i >= 70:
            grade = 3.0
        elif i >= 65:
            grade = 2.5
        elif i >= 60:
            grade = 2.0
        elif i >= 55:
            grade = 1.5
        elif i >= 50:
            grade = 1
        elif i < 50:
            grade = 0
        sum = sum + grade * 3.0
        unit_count = unit_count + 1
    return sum/(unit_count * 3)
def save_data():
    with open("db.txt", 'w') as f:
        for i in database:
            key = i
            info = database[i]
            string = ""
            string = key + "#"
            for j in info:
                string = string + str(j) + "#"
            f.write(string + "\n")
def insert_data():
    Exit = 'n'
    while Exit == 'n':
        sid = input("Enter student SID:")
        name = input("Enter student Name:")
        email = input("Enter student Email:")
        math_score = float(input("Enter Math score:"))
        physics_score = float(input("Enter Physics score:"))
        computer_score = float(input("Enter Computer score:"))
        scores = [math_score, physics_score, computer_score]
        gpa = GPA(scores)
        information = [name, email, math_score, physics_score, computer_score, gpa]
        database[sid] = information
        print(database)
        Exit = input("Exit from insert data[y/n]:")
    else:
        save_data()
        print("Exit form insert data!")
def del_data():
    sid = input("Enter the student SID that you want to delete:")
    if sid in database:
        del database[sid]
        print("The", sid, "has been deleted")
    else:
        print(sid ," not found!")
        return
    save_data()    
    
database = {}
menu()
choice = int(input("Enter your choice ="))
while choice != 0:
    if choice == 1:
        insert_data()
    elif choice == 2:
        del_data()
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

    
