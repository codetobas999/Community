def writebookfile(data):
    filename = 'book.txt'
    try:
        file = open(filename, 'a')
        file.write(data)
        file.close()
        return True
    except IOError as e:
        print(e)
        file.close()
        return False

def updatebookfile(bookid, status):
    filename = 'book.txt'
    try:
        result = []
        with open(filename, 'r') as file:
            readmsg = file.readlines()
            for data in readmsg:
                readmsg = data.rstrip("\n")
                msg = readmsg
                result.append(msg)

        file = open(filename, 'w')
        for i in range(0, len(result)):
            data = result[i][0:4]
            if data == bookid:
                if status == 1:
                    new = '0'
                if status == 2:
                    new = '1'
                msg = result[i][0:len(result[i])-1] + new + "\n"
            else:
                msg = result[i] + "\n"
            file.write(msg)
        file.close()
        return True
    except IOError as e:
        print(e)
        file.close()
        return False

def searchbookdata(bookdata):
    filename = 'book.txt'
    try:
        check = False
        with open(filename, 'r') as file:
            readmsg = file.readlines()
            for data in readmsg:
                readmsg = data.rstrip("\n")
                result = readmsg.split(';',3)
                if result[0] == bookdata[0] or result[1] == bookdata[1]:
                    check = True
            file.close()
        return check
    except IOError as e:
        print(e)
        return False

def searchbooklist():
    filename = 'book.txt'
    try:
        result = ['รหัสหนังสือ;ชื่อหนังสือ']
        with open(filename, 'r') as file:
            readmsg = file.readlines()
            for data in readmsg:
                readmsg = data.rstrip("\n")
                msg = readmsg
                if msg[len(msg)-1] == "1":
                    result.append(msg[0:len(msg)-2])
            file.close()
        return result
    except IOError as e:
        print(e)
        return False

def writeborrowfile(data):
    filename = 'borrow.txt'
    try:
        file = open(filename, 'a')
        file.write(data)
        file.close()
        return True
    except IOError as e:
        print(e)
        return False

def updateborrowfile(sno, bookid):
    filename = 'borrow.txt'
    try:
        result = []
        with open(filename, 'r') as file:
            readmsg = file.readlines()
            for data in readmsg:
                readmsg = data.rstrip("\n")
                msg = readmsg
                result.append(msg)

        file = open(filename, 'w')
        for i in range(0, len(result)):
            data1 = result[i][0:5]
            data2 = result[i][11:15]
            if data1 == sno and data2 == bookid:
                new = '1'
                msg = result[i][0:len(result[i])-1] + new + "\n"
            else:
                msg = result[i] + "\n"
            file.write(msg)
        file.close()
        return True
    except IOError as e:
        print(e)
        return False

def searchslipno():
    filename = 'borrow.txt'
    try:
        result = []
        with open(filename, 'r') as file:
            readmsg = file.readlines()
            for data in readmsg:
                readmsg = data.rstrip("\n")
                result = readmsg[0:5]
            file.close()
        return result
    except IOError as e:
        print(e)
        return False

def searchborrow(var, sdata):
    filename = 'borrow.txt'
    try:
        result = ['รายชื่อหนังสือที่ยืม']
        with open(filename, 'r') as file:
            readmsg = file.readlines()
            for data in readmsg:
                readmsg = data.rstrip("\n")
                msg = readmsg.split(';', 5)
                if msg[4] == '0':
                    if var == 1:
                        if msg[1] == sdata:
                            result.append(readmsg[0:len(readmsg)-2])
                    if var == 2:
                        if msg[0] == sdata:
                            result.append(readmsg[0:len(readmsg)-2])
            file.close()
        return result
    except IOError as e:
        print(e)
        return False

def searchmember():
    filename = 'member.txt'
    try:
        result = ['รายชื่อสมาชิก']
        with open(filename, 'r') as file:
            readmsg = file.readlines()
            for data in readmsg:
                result.append(data.rstrip("\n"))
            file.close()
        return result
    except IOError as e:
        print(e)
