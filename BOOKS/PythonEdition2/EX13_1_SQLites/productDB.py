import sqlite3

def createtable():
    try:
        con = sqlite3.connect('productDB.db')
        sql = 'CREATE TABLE IF NOT EXISTS product ' \
              '(pid INT PRIMARY KEY NOT NULL, ' \
              'pname TEXT, totalA INT, totalB INT, ' \
              'pprice REAL);'
        con.execute(sql)
        con.commit()
        sql = 'CREATE TABLE IF NOT EXISTS transfer ' \
                    '(tid TEXT PRIMARY KEY NOT NULL , ' \
                    'pid TEXT, pqty INT);'
        con.execute(sql)
        con.commit()
    except con.Error as e:
        if con:
            print("error is " + e)
    con.close()

def insertproducttable(*data):
    try:
        con = sqlite3.connect('productDB.db')
        sql = 'INSERT INTO product (pid, pname, totalA, totalB) ' \
              'VALUES ("' + data[0] + '","' + data[1] + '",' + \
              str(data[2]) + ',' + str(data[3]) + ')'
        con.execute(sql)
        con.commit()
        return True
    except con.Error as e:
        if con:
            print("error is " + e)
            return False
    con.close()

def updateproducttable(*data):
    try:
        con = sqlite3.connect('productDB.db')
        sql = 'UPDATE product SET pname =  "' + data[1] + \
              '", totalA =  ' + str(data[2]) + \
              ', totalB =  ' + str(data[3]) + \
              ' WHERE pid = "' + data[0] + '"'
        con.execute(sql)
        con.commit()
        return True
    except con.Error as e:
        if con:
            print("error is " + e)
            return False
    con.close()

def selectproductid():
    try:
        con = sqlite3.connect('productDB.db')
        sql = 'SELECT pid FROM product order by pid'
        data = con.execute(sql)
        result = False
        for row in data:
            result = row[0]
        return result
    except con.Error as e:
        if con:
            print("error is " + e)
    finally:
        if con:
            con.close()

def selectproductname(productname):
    try:
        con = sqlite3.connect('productDB.db')
        sql = 'SELECT * FROM product WHERE pname = "' + \
              productname + '"'
        data = con.execute(sql)
        result = False
        for row in data:
            result = True
        return result
    except con.Error as e:
        if con:
            print("error is " + e)
    finally:
        if con:
            con.close()

def selectproducttable():
    try:
        con = sqlite3.connect('productDB.db')
        sql = 'SELECT * FROM product'
        data = con.execute(sql)
        result = ['รหัส:ชื่อ:สินค้าคลัง A:สินค้าคลัง B']
        for row in data:
            result.append(row[0]+':'+row[1]+':'+str(row[2])+':'+str(row[3]))

        return result
    except con.Error as e:
        if con:
            print("error is " + e)
    finally:
        if con:
            con.close()

def inserttransfertable(*data):
    try:
        con = sqlite3.connect('productDB.db')
        sql = 'INSERT INTO transfer ' \
              '(tid, pid, pqty) ' \
              'VALUES ("' + data[0] + '","' + data[1] + \
              '",' + str(data[2]) + ')'
        con.execute(sql)
        con.commit()
    except con.Error as e:
        if con:
            print("error is " + e)
    con.close()

def selecttransfertable(status):
    try:
        con = sqlite3.connect('productDB.db')
        sql = 'SELECT transfer.tid, transfer.pid, product.pname, ' \
              'transfer.pqty FROM transfer, product where ' \
              'transfer.pid = product.pid and transfer.tid like "%' + \
              status + '"'
        data = con.execute(sql)
        result = ['รหัสการโอนย้าย:รหัสสินค้า:ชื่อสินค้า:จำนวน']
        for row in data:
            tid = row[0]
            result.append(tid[0:4]+':'+row[1]+':'+ row[2]+':'+str(row[3]))
            
        return result
    except con.Error as e:
        if con:
            print("error is " + e)
    finally:
        if con:
            con.close()

def selecttransferid():
    try:
        con = sqlite3.connect('productDB.db')
        sql = 'SELECT tid FROM transfer order by tid'
        data = con.execute(sql)
        result = False
        for row in data:
            result = row[0]
        return result
    except con.Error as e:
        if con:
            print("error is " + e)
    finally:
        if con:
            con.close()
