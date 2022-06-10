import pymysql

def createdatabase():
    try:
        host = "localhost"
        user = "root"
        pw = ""
        dbname = "cakesdb"
        conn = pymysql.connect(host, user, pw)
        cur = conn.cursor()
        cur.execute("SHOW DATABASES")
        result = False
        for x in cur:
            if dbname in x:
                result = True
        if not result:
            cur.execute("CREATE DATABASE cakesDB")
        conn.close()
    except Exception as e:
        print(e)

def createtable():
    try:
        host = "localhost"
        user = "root"
        pw = ""
        dbname = "cakesDB"
        conn = pymysql.connect(host, user, pw, dbname)
        cur = conn.cursor()
        sql = "USE " + dbname
        cur.execute(sql)
        cur.execute("SHOW TABLES")
        tblname = 'product'
        result = False
        for x in cur:
            if tblname in x:
                result = True
        if not result:
            sql = "CREATE TABLE product " \
                  "(pid INT PRIMARY KEY NOT NULL AUTO_INCREMENT, " \
                  "pname VARCHAR(50), pqty INT, ismilk VARCHAR(1), " \
                  "isbutter VARCHAR(1), isnut VARCHAR(1))"
            cur.execute(sql)
        conn.close()
    except Exception as e:
        print(e)

def insertproducttable(*data):
    host = "localhost"
    user = "root"
    pw = ""
    dbname = "cakesDB"
    conn = pymysql.connect(host, user, pw, dbname)
    cur = conn.cursor()
    sql = "INSERT INTO product " \
          "(pname, pqty, ismilk, isbutter, isnut) VALUES (" \
          "'" + data[0] + "'," + str(data[1]) + ",'" \
          + data[2] + "','" + data[3] + "','" \
          + data[4] + "')"
    print(sql)
    try:
        cur.execute(sql)
        conn.commit()
        return True
    except Exception as e:
        print(e)
        conn.rollback()
        return False
    conn.close()

def updateproducttable(*data):
    host = "localhost"
    user = "root"
    pw = ""
    dbname = "cakesDB"
    conn = pymysql.connect(host, user, pw, dbname)
    cur = conn.cursor()
    sql = "UPDATE product SET pqty =  " + str(data[1]) + \
          " WHERE pid = " + str(data[0])
    try:
        cur.execute(sql)
        conn.commit()
        return True
    except Exception as e:
        print(e)
        conn.rollback()
        return False
    conn.close()

def selectproductname(productname):
    try:
        host = "localhost"
        user = "root"
        pw = ""
        dbname = "cakesDB"
        conn = pymysql.connect(host, user, pw, dbname)
        cur = conn.cursor()
        sql = "USE " + dbname
        cur.execute(sql)
        sql = "SELECT * FROM product WHERE pname = '" + \
              productname + "'"
        cur.execute(sql)
        data = cur.fetchall()
        if len(data) == 0:
            result = False
        else:
            result = True
        return result
    except Exception as e:
        print(e)

def selectproducttable(sdata):
    host = "localhost"
    user = "root"
    pw = ""
    dbname = "cakesDB"
    conn = pymysql.connect(host, user, pw, dbname)
    cur = conn.cursor()
    sql = "SELECT * FROM product"
    try:
        cur.execute(sql)
        data = cur.fetchall()
        if sdata == 0:
            result = ["รหัส:ชื่อ:จำนวนสินค้าคลัง"]
        else:
            result = ["ชื่อ:จำนวนสินค้าคลัง:เนย:นม:ถั่ว"]
        for row in data:
            if sdata == 0:
                result.append(str(row[0]) + ':' + row[1] + ':' + str(row[2]))

            else:
                result.append(row[1] + ':' + str(row[2])
                              + ':' + str(row[3]) + ':' + str(row[4]) + ':' + str(row[5]))
        return result
    except Exception as e:
        print(e)
    conn.close()
