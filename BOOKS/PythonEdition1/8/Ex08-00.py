"""
my_lines = []
flag = True
while(flag):
    try:
        line = input()
        line.rstrip()
        my_lines.append(line)
    except EOFError as e:
        print("EOFError" , e)
        flag = False

print ("Let us print list of lines")

for l in my_lines:
    print (l)
"""
age = -1   # an initially invalid choice
while age <= 0:
    try:
        age = int(input('Enter your age in years: '))
        if age <= 0:
            print('Your age must be positive.')
    except ValueError:
        print('That is an invalid age specification.')
    except EOFError:
        print('There was an unexpected error reading input.')
        age = 1

