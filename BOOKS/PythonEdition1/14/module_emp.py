import sqlite3


def insertemployee(empid, emppw, emptype):
    con = sqlite3.connect('stockDB.db')
    try:
        sql = 'insert into employee (empid, emppw, emptype) ' \
              'VALUES("' + empid + '", "' + emppw + '" ,' \
              + str(emptype) + ')'
        con.execute(sql)
        con.commit()
    except con.Error as e:
        if con:
            print("error is ", e)
            con.rollback()
    finally:
        if con:
            con.close()


def updateemployee(empid, emppw, emptype):
    con = sqlite3.connect('stockDB.db')
    try:
        sql = 'UPDATE employee SET emppw = "' + emppw + '",  ' \
            'emptype = ' + str(emptype) + \
            ' WHERE empid = "' + empid + '"'
        con.execute(sql)
        con.commit()
    except con.Error as e:
        if con:
            print("error is ", e)
            con.rollback()
    finally:
        if con:
            con.close()


def deleteemployee(empid, active):
    con = sqlite3.connect('stockDB.db')
    try:
        if active == 0:
            sql = 'DELETE FROM employee ' \
                  'WHERE empid = "' + empid + '"'
        else:
            sql = 'UPDATE employee SET empdelete = 0 ' \
                  'WHERE empid = "' + empid + '"'
        con.execute(sql)
        con.commit()
    except con.Error as e:
        if con:
            print("error is ", e)
            con.rollback()
    finally:
        if con:
            con.close()


def selectlastemployeeid():
    con = sqlite3.connect('stockDB.db')
    try:
        result = 0
        sql = 'SELECT * FROM employee WHERE empdelete = 1 ' \
                'ORDER BY empid'
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


def selectemployee(empid, emppw):
    con = sqlite3.connect('stockDB.db')
    try:
        sql = 'SELECT * FROM employee ' \
                'WHERE empid = "' + empid + '" ' \
                'AND emppw = "' + emppw + '" ' \
                'AND empdelete = 1'
        data = con.execute(sql)
        result = list()
        for row in data:
            result.append(row)
        if len(result) == 0:
            result = False
        return result
    except con.Error as e:
        if con:
            print("error is ", e)
    finally:
        if con:
            con.close()

def selectallemployee(no):
    con = sqlite3.connect('stockDB.db')
    try:
        if no == 0:
            sql = 'SELECT * FROM employee ' \
                'ORDER BY empid'
        else:
            sql = 'SELECT * FROM employee WHERE empdelete = 1 ' \
                'ORDER BY empid'

        data = con.execute(sql)
        result = list()
        title = 'EMPLOYEE  DATA'
        result.append(title)
        result.append('='*35)
        heading = '(ID) (Password) (Type) (Status)'
        result.append(heading)
        for row in data:
            if row[2] == 1:
                emptype = 'admin'
            else:
                emptype = 'user'
            if row[3] == 1:
                active = 'active'
            else:
                active = 'inactive'
            msg = "({:s}) ({:s}) ({:s}) ({:s})".format(row[0], row[1], emptype, active)
            result.append(msg)
        if len(result) == 3:
            result.remove(heading)
            result.append('No Data')
        result.append('='*35)
        if len(result) > 4:
            sum_sql = 'SELECT count(empid)  ' \
                  ' FROM employee where emptype = 1 and empdelete = 1'
            sum_data = con.execute(sum_sql)
            count1 = 0
            for row in sum_data:
                count1 = row[0]
            sum_sql = 'SELECT count(empid)  ' \
                      'FROM employee where emptype = 2  and empdelete = 1'
            sum_data = con.execute(sum_sql)
            count2 = 0
            for row in sum_data:
                count2 = row[0]
            footer = "admin = {:d} persons, user = {:d} persons".format(count1, count2)
            result.append(footer)
            footer = "total employee = {:d} persons".format(count1+count2)
            result.append(footer)
            result.append('='*35)
        return result
    except con.Error as e:
        if con:
            print("error is ", e)
    finally:
        if con:
            con.close()


def printempqry(data):
    msg = ''
    for row in data:
            msg = msg + str(row) + "\n"
    return msg
