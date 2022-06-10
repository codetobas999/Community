DayOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
day = input("Enter the date: ")
for day_x in DayOfWeek:
    if day == day_x:
        print("Found : ", day_x)
        break
    else:
        print("Not found :", day_x)
    
        
