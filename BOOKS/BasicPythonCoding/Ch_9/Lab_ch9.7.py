def switch(choice):
    case = ""
    if(choice == 0):
        case = "zero"
    elif(choice == 1):
        case = "one"
    elif(choice == 2):
        case = "two"
    else:
        case = "nothing"
    return case

print(switch(0))
print(switch(1))
print(switch(2))
print(switch(3))
