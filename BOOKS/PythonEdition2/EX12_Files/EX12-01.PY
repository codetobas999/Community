filename = "D:/file01.txt"
try:
    file = open(filename, 'a')
    file.write("m001;Anna"+"\n")
    file.write("m002;Anan"+"\n")
    file.close()
except IOError as e:
    print(e)
