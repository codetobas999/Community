filename = "D:/file01.txt"
try:
    with open(filename, 'r') as file:
        readmsg = file.readlines()
        result = []
        for data in readmsg:
            result.append(data.rstrip("\n"))
    for msg in result:
        print(msg)
    file.close()
except IOError as e:
    print(e)

