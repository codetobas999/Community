def switch(choice): 
    case = { 
        0: "zero", 
        1: "one", 
        2: "two"} 
  
    return case.get(choice, "nothing") 

print(switch(0))
print(switch(1))
print(switch(2))
print(switch(3)) 
