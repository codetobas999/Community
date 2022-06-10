def insert_data(n):
    print("------------------------")
    print("The student number: ",n)
    sid = input("Enter student SID:")
    name = input("Enter student Name:")
    email = input("Enter student Email:")
    phone = input("Enter student Phone:")
    math_score = float(input("1. Enter Math score:"))
    physics_score = float(input("2. Enter Physics score:"))
    computer_score = float(input("3. Enter Computer score:"))
    music = float(input("4. Enter Music score:"))
    chemistry = float(input("5. Enter Chemistry score:"))
    art = float(input("6. Enter Art score:"))
    english = float(input("7. Enter English score:"))
    agriculture = float(input("8. Enter Agriculture score:"))
    sport = float(input("9. Enter Sport score:"))
    science = float(input("10. Enter Science score:"))
    information = [name, email, phone, math_score, physics_score, computer_score, music, chemistry, art, english, agriculture, sport, science]
    database[sid] = information

database = {}
n = int(input("Enter the number of students: "))
while n > 0:
    insert_data(n)
    n = n - 1

print(database)
