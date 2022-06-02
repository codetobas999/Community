import sqlite3
from sqlite3 import Error
from datetime import datetime, timezone

database = r"D:\BAS\WORKSPACE\PYTHON\HEROKU\bas2bot\db\portfolio.db"
sql_coins_tbl      = """ CREATE TABLE IF NOT EXISTS coins (coin_code text PRIMARY KEY,coin_desc text,priority integer,status text,status_dtm timestamp); """
sql_variables_tbl  = """ CREATE TABLE IF NOT EXISTS variables (key text PRIMARY KEY,value text,data_group text,status text,status_dtm timestamp); """
sql_signals_tbl     = """ CREATE TABLE IF NOT EXISTS signals (coin_code text, recommen text,gauge_buy decimal ,gauge_sell decimal ,gauge_neutral decimal ,price decimal, rsi decimal,macd decimal,macd_signal decimal,sma5 decimal,sma10 decimal,sma20 decimal,sma30 decimal,sma50 decimal,sma100 decimal,sma200 decimal,ema5 decimal,ema10 decimal,ema20 decimal,ema30 decimal,ema50 decimal,ema100 decimal,ema200 decimal,fibonacci_s3 decimal,fibonacci_s2 decimal,fibonacci_s1 decimal,fibonacci_m decimal,fibonacci_r1 decimal,fibonacci_r2 decimal,fibonacci_r3 decimal,signal_dtm timestamp, trade_dtm timestamp ,status text,status_dtm timestamp); """
sql_trades_tbl     = """ CREATE TABLE IF NOT EXISTS trades (coin_code text, recommen  text ,gauge_buy decimal ,gauge_sell decimal ,gauge_neutral decimal ,price decimal,unit decimal,rsi decimal,sma5 decimal,sma10 decimal,sma20 decimal,signal_dtm timestamp, trade_dtm timestamp ,status text,status_dtm timestamp); """
#sql_trades_tbl     = """ CREATE TABLE IF NOT EXISTS trades (coin_code text,action text,price decimal,unit decimal,rsi decimal,sma5 decimal,sma10 decimal,sma20 decimal,status text); """
sql_wallets_tbl    = """ CREATE TABLE IF NOT EXISTS wallets (coin_code text,coin_value decimal,balance decimal, status text,status_dtm timestamp); """
sql_portfolios_tbl = """ CREATE TABLE IF NOT EXISTS portfolios (coin_code text,unit decimal,status text,status_dtm timestamp); """

sql_inst_coins      = "INSERT INTO coins(coin_code,coin_desc,priority,status,status_dtm) values (?,?,?,?,datetime('now', 'localtime'))"
sql_inst_variables  = "INSERT INTO variables((key,value,data_group,status,status_dtm) values (?,?,?,,datetime('now', 'localtime'))"
sql_inst_signals     = "INSERT INTO signals(coin_code,recommen ,gauge_buy,gauge_sell,gauge_neutral,price,rsi,macd,macd_signal,sma5,sma10,sma20,sma30,sma50,sma100,sma200,ema5,ema10,ema20,ema30,ema50,ema100,ema200,fibonacci_s3,fibonacci_s2,fibonacci_s1,fibonacci_m,fibonacci_r1,fibonacci_r2,fibonacci_r3,status,signal_dtm,trade_dtm,status_dtm) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,datetime('now', 'localtime'),datetime('now', 'localtime'))"
sql_inst_trades     = "INSERT INTO trades(coin_code,recommen ,gauge_buy ,gauge_sell ,gauge_neutral ,price,unit,rsi,sma5,sma10,sma20,status,signal_dtm,trade_dtm,status_dtm) values (?,?,?,?,?,?,?,?,?,?,?,?,?,datetime('now', 'localtime'),datetime('now', 'localtime'))"
#sql_inst_trades     = "INSERT INTO trades(coin_code,action,price,unit,rsi,sma5,sma10,sma20,status,trade_dtm,status_dtm) values (?,?,?,?,?,?,?,?,?)"
sql_inst_wallets    = "INSERT INTO wallets(coin_code,coin_value,balance,status,status_dtm) values (?,?,?,?,,datetime('now', 'localtime'))"
sql_inst_portfolios = "INSERT INTO portfolios(coin_code,unit,status,status_dtm) values (?,?,?,,datetime('now', 'localtime'))"

#sql_check_trade     = "select coin_code||\'-\'||action || \'-\' || rsi || \'-\' || sma5 || \'-\' || sma10 || \'-\' || sma20  Result from (select * from trades where coin_code = '#coin#'  order by trade_dtm desc) LIMIT 1"
sql_last_signal_by_coin     = "select * from (select * from signals where coin_code = '#coin#'  order by signal_dtm desc) LIMIT 1"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def get_connection(): 
    conn = None
    try:
        conn = create_connection(database)
        create_table(conn, sql_coins_tbl)
        create_table(conn, sql_variables_tbl)
        create_table(conn, sql_signals_tbl)
        create_table(conn, sql_trades_tbl)
        create_table(conn, sql_wallets_tbl)
        create_table(conn, sql_portfolios_tbl)
        #print("get_connection OK.")
    except Error as e:
        print(e) 
    return conn

def sysdate():  
    return datetime.now(timezone.utc)

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
 
def insert_data(conn,sql_inst,data):
    conn.executemany(sql_inst,data)  
    conn.commit()
    print("Total Insert of rows  [{}]".format(conn.total_changes)) 

def check_data_exists(conn,sql_check,str_check):
    #sceeb = int(raw_input(":> "))
    records = conn.execute(sql_check).fetchall() 
    print("Total rows are:  ", len(records))  
    if len(records) == 1 and records[0][0] == str_check : 
        print("Data Compare  [{}] vs [{}]".format(records[0][0] , str_check) )
        return True
    else : 
        return False 

def get_single_record(conn,sql_check):
    #sceeb = int(raw_input(":> "))
    records = conn.execute(sql_check).fetchall() 
    #print("Total rows are:  ", len(records))  
    if len(records) == 1 : 
        return records[0]
    else : 
        return []      

def main():  
    # create a database connection
    conn = get_connection()

    # create tables
    if conn is not None:
        # create projects table
        #create_table(conn, sql_coins_tbl)
        #create_table(conn, sql_variables_tbl)
        #create_table(conn, sql_trades_tbl)
        #create_table(conn, sql_wallets_tbl)
        #create_table(conn, sql_portfolios_tbl)

        rec = []
        data = []
        #print("----------------- inst_trades : [{}] -----------------".format(coin))
        
        rec.append('BTCUSDT')
        rec.append('XX')
        rec.append(0.9)
        rec.append(0.01)
        rec.append(0.8)
        rec.append(0.8)
        rec.append(0.8)
        rec.append(0.8)
        rec.append("ACTIVE")
        rec.append("2012-12-25 23:59:59") 
        data.append(rec)
        insert_data(conn,sql_inst_trades,data)


        #insert_data(conn,sql_inst_coins,coin)
        #print(777)
        #coin = 'BTCUSDT'
        #sql  = sql_last_trade_by_coin.replace("#coin#", coin)
        #print("sql_last_trade_by_coin  [{}]".format(sql)) 
        #data = get_single_record(conn,sql)
        #if len(data) > 0: 
        #    print(data)
        #if check_data_exists(conn,'select coin_code||\'-\'||action || \'-\' || rsi || \'-\' || sma5 || \'-\' || sma10 || \'-\' || sma20 Result from (select * from trades order by trade_dtm desc) LIMIT 1','BTCUSDT-STRONG_SELL-33.17797162-59606.73-59679.289-59684.068x') :
        #   print(999)
        #else :
        #   print(888) 


    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
