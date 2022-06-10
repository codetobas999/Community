from pathlib import Path
import pyodbc
import pypyodbc

dbname = "D:/signupDB.mdb"
constr = "Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq="
tblname = "signup"
conname = constr + dbname

def createdatabase():
    dbpath = Path(dbname)
    try:
        if not dbpath.is_file():
            pypyodbc.win_create_mdb(dbname)
            print("'" + dbname + "' is created")
    except Exception as e:
        print(e)

def createtable():
    try:
        conn = pyodbc.connect(conname, autocommit=True)
        cur = conn.cursor()
        check = False
        if cur.tables(table=tblname, tableType='TABLE').fetchone():
            check = True
        if not check:
            sql = "CREATE TABLE " + tblname + \
                  "(uname TEXT(8) PRIMARY KEY NOT NULL, " \
                  "upass TEXT(8))"
            cur.execute(sql)
            print(tblname, "is created")
    except Exception as e:
        print(e)

def insertsignup(*data):
    try:
        conn = pyodbc.connect(conname, autocommit=True)
        cur = conn.cursor()
        sql = "INSERT INTO " + tblname + " (uname, upass) VALUES " \
              "('" + data[0] + "','" + data[1] + "')"
        cur.execute(sql)
        return True
    except Exception as e:
        print(e)
        return False

def updatesignup(*data):
    try:
        conn = pyodbc.connect(conname, autocommit=True)
        cur = conn.cursor()

        sql = "UPDATE " + tblname + " SET upass =  '" + data[1] + \
              "' WHERE uname = '" + data[0] + "'"
        cur.execute(sql)
        return True
    except Exception as e:
        print(e)
        return False

def selectsignup(*data):
    try:
        conn = pyodbc.connect(conname, autocommit=True)
        cur = conn.cursor()
        sql = "SELECT * FROM " + tblname + " WHERE uname='" + data[0] + \
              "' AND signup.upass='" + data[1] + "'"
        data = cur.execute(sql)
        result = False
        for row in data:
            result = row[0] + ';' + row[1]
        return result
    except Exception as e:
        print(e)

def selectuname(username):
    try:
        conn = pyodbc.connect(conname, autocommit=True)
        cur = conn.cursor()

        sql = "SELECT * FROM signup WHERE uname='" + username + "'"
        data = cur.execute(sql)
        result = False
        for row in data:
            result = row[0]
        return result
    except Exception as e:
            print(e)
