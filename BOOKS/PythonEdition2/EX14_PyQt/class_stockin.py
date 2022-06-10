import sqlite3


def insertstockin(stdate, pid, empid, stqty, stcost):
    con = sqlite3.connect('productstock.db')
    try:
        sql = 'INSERT INTO stockin (stdate, pid, empid, stqty, stcost) ' \
              'VALUES ("' + stdate + '", "' + pid + '", "' + empid + '", ' + \
              str(stqty) + ',' + str(stcost) + ')'
        con.execute(sql)
        con.commit()
    except con.Error as e:
        if con:
            print("error is ", e)
            con.rollback()
    finally:
        if con:
            con.close()


def selectallstockin(no):
    con = sqlite3.connect('productstock.db')
    try:
        if no == 1:
            sql = 'SELECT stockin.pid, product.pname, ' \
                'sum(stockin.stqty), avg(stockin.stcost) ' \
                'FROM stockin, product ' \
                'WHERE stockin.pid = product.pid ' \
                'GROUP BY stockin.pid ORDER BY stockin.pid'
        else:
            sql = 'SELECT stockin.stdate, stockin.pid, ' \
                'product.pname, stockin.stqty, stockin.stcost ' \
                'FROM stockin, product ' \
                'WHERE stockin.pid = product.pid ' \
                'ORDER BY stockin.pid'


        data = con.execute(sql)
        result = list()
        title = 'STOCK IN DATA'
        result.append(title)
        result.append('='*40)
        if no == 1:
            heading = '(ID) (Name) (Quantity) (Cost)'
        else:
            heading = '(Date) (ID) (Name) (Quantity) (Cost)'
        result.append(heading)
        for row in data:
            if no == 1:
                msg = '({:s}) ({:s}) ({:,d}) ({:,.2f})'.format(row[0], row[1], int(row[2]), float(row[3]))
            else:
                msg = '({:s}) ({:s}) ({:s}) ({:,d}) ({:,.2f})'.format(row[0], row[1], row[2],  int(row[3]), float(row[4]))

            result.append(msg)
        if len(result) == 3:
            result.remove(heading)
            result.append('No Data')
        result.append('='*40)
        return result
    except con.Error as e:
        if con:
            print("error is ", e)
    finally:
        if con:
            con.close()


def printstockinqry(data):
    msg = ''
    for row in data:
        msg = msg + str(row) + "\n"
    return msg

