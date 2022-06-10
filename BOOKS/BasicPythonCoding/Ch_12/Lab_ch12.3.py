with open("myfile.txt", 'r') as f:

    for string in f:
        line = string.strip()
        print(line)


with open("myfile.txt", 'r') as f:

    while True:
        string = f.readline()
        line = string.strip()
        if line == '':
            break
        print(line)
    
