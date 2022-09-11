def read_file(file_name): 
    f = open(file_name, "r")
    str = ''
    while(True):
        #read next line
        line = f.readline()
        #if line is empty, you are done with all lines in the file
        if not line:
            break
        #you can access the line
        #print(line.strip())
        str = str + line.strip() 
    #close file
    f.close
    return str
