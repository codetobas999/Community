import sqlite3


def createTable():
    con = sqlite3.connect('productstock.db')
    try:
        sql = 'CREATE TABLE IF NOT EXISTS product ' \
              '(pid TEXT PRIMARY KEY NOT NULL, ' \
              'pname TEXT, pqty INT, pcost REAL, ' \
              'ppic TEXT)'
        con.execute(sql)

        sql = 'CREATE TABLE IF NOT EXISTS ' \
              'member (mid TEXT PRIMARY KEY NOT NULL, ' \
              'mname TEXT, mads TEXT, mtype INT)'
        con.execute(sql)

        sql = 'CREATE TABLE IF NOT EXISTS ' \
              'employee (empid TEXT PRIMARY KEY NOT NULL, ' \
              'emppw TEXT,  emptype INT, ' \
              'empdelete INT NOT NULL DEFAULT 1)'
        con.execute(sql)

        sql = 'CREATE TABLE IF NOT EXISTS stockin ' \
              '(stno INTEGER PRIMARY KEY  AUTOINCREMENT NOT NULL, ' \
              'stdate TEXT, pid TEXT, empid TEXT, stqty INT, stcost REAL)'
        con.execute(sql)
    except con.Error as e:
        if con:
            print('error is', e)
    con.close()
