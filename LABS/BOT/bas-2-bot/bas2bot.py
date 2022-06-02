#heroku ps:scale bas2bot=1
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from binance_connect import SIGNALS_BY_SYMBOL_TDV , SIGNALS_BY_SYMBOL
from db_connect import * 
sched = BlockingScheduler()
g_time           = int(os.environ['G_TIME'])
g_max_instances  = int(os.environ['G_MAX_INSTANCES'])
g_coins          = os.environ['G_COINS']  
#g_coins          = "BTCUSDT" 
#g_time = 3           #ENV['G_TIME']
#g_max_instances = 5  #ENV['G_MAX_INSTANCES']
#g_coin = 'BTCUSDT'   #ENV['G_COIN']  
print("g_time [{}] , g_max_instances [{}] , g_coin [{}]".format( g_time , g_max_instances , g_coins)) 
@sched.scheduled_job('interval', seconds= g_time , max_instances=g_max_instances)
def timed_job():
    #print('This job is run every three second.')
    #print("CHECKING FOR SIGNALS PLEASE WAIT")
    #coin_list = ["BTCUSDT"] #, "BTCUSDT","DOTUSDT","BNBUSDT","MATICUSDT"
      
    #coin = [['BTCUSDT', 'BUY', 58657.65, 0.01, 54.53551965, 58632.458, 58638.97, 58623.534, 'ACTIVE']]
    #conn = get_connection()
    #insert_data(conn,sql_inst_trades,coin)
    #for coin in coin_list :
        #result = SIGNALS_BY_SYMBOL_TDV(coin) 
    coin_list = g_coins.split(",")    
    for coin in coin_list : 
        SIGNALS_BY_SYMBOL_TDV(coin) 
        #SIGNALS_BY_SYMBOL(coin) 
        #print("result {}".format( result))
        #insert_data(conn,sql_inst_trades,result)

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start() 