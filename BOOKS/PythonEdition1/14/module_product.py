import sqlite3


def insertproduct(id, name, qty, cost, pic):
    con = sqlite3.connect('stockDB.db')
    try:
        sql = 'INSERT INTO product ' \
              '(pid, pname, pqty, pcost, ppic) ' \
              'VALUES ("' + id + '","' + name + '",' + \
              str(qty) + ','  + str(cost) + \
              ',"' + pic + '")'
        con.execute(sql)
        con.commit()
    except con.Error as e:
        if con:
            print('error is', e)
            con.rollback()
    finally:
        if con:
            con.close()


def updateproduct(id, name, qty, cost, pic):
    con = sqlite3.connect('stockDB.db')
    try:
        sql = 'UPDATE product SET pname = "' + name  + \
              '", pqty = ' + str(qty) + \
              ', pcost = ' + str(cost) + \
              ', ppic = "' + pic + \
              '"  WHERE pid = "' + id + '"'
        con.execute(sql)
        con.commit()
    except con.Error as e:
        if con:
            print("error is ", e)
            con.rollback()
    finally:
        if con:
            con.close()


def selectlastproductid():
    con = sqlite3.connect('stockDB.db')
    try:
        result = 0
        sql = 'SELECT * FROM product ORDER BY pid'
        data = con.execute(sql)
        for row in data:
            result = row[0]
        return result
    except con.Error as e:
        if con:
            print("error is ", e)
    finally:
        if con:
            con.close()


def selectproduct(id):
    con = sqlite3.connect('stockDB.db')
    try:
        sql = 'SELECT * FROM product WHERE pid = "' + id + '"'
        data = con.execute(sql)
        result = list()
        for row in data:
            result.append(row)
        return result
    except con.Error as e:
        if con:
            print("error is ", e)
    finally:
        if con:
            con.close()


def selectallproduct(no):
    con = sqlite3.connect('stockDB.db')
    try:
        sql = 'SELECT * FROM product ORDER BY pid'
        data = con.execute(sql)
        result = list()
        title = ' PRODUCT DATA'
        result.append(title)
        result.append('='*40)
        heading = '(ID) (Name) (Quantity) (Cost)'
        result.append(heading)
        for row in data:
            if no == 1:
                msg = '({:s}) ({:s}) ({:,d}) ({:,.2f})'.format(row[0], row[1], int(row[2]), float(row[3]))
            else:
                msg = '({:s}) ({:s}) ({:,d}) ({:,.2f}) ({:s})'.format(row[0], row[1], int(row[2]),  float(row[3]), row[4])
            result.append(msg)
        if len(result) == 3:
            result.remove(heading)
            result.append('No Data')
        result.append('='*40)
        if len(result) > 4:
            sum_sql = 'SELECT sum(pqty),  ' \
                  'sum(pqty*pcost) FROM product'
            sum_data = con.execute(sum_sql)
            total_sum = 0
            for row in sum_data:
                total_sum = row
            footer = "total quantity = {:,.0f} pieces".format(total_sum[0])
            result.append(footer)
            footer = "total cost = {:,.2f} baht".format(total_sum[1])
            result.append(footer)
            result.append('='*40)
        return result
    except con.Error as e:
        if con:
            print("error is ", e)
    finally:
        if con:
            con.close()


def printproductqry(data):
    msg = ''
    for row in data:
        msg = msg + str(row) + "\n"
    return msg
