#https://github.com/jp-developer0/Python-TradingView-TA-Library
#https://www.youtube.com/watch?v=LQQGSibtjfM
#https://developers.line.biz/media/messaging-api/emoji-list.pdf
#http://cons-robotics.com/LINEAPI/sticker.pdf
#https://unicode.org/emoji/charts-11.0/emoji-list.html
#----
from songline import Sendline
#----
from tradingview_ta import TA_Handler, Interval
import time
from datetime import datetime
import config
from binance.client import Client
from binance.enums import * 
#----  
import matplotlib.pyplot as plt
import numpy as np
import talib as ta  
#-------------------------------------
from db_connect import * 
#-------------------------------------
now = datetime.now()
fecha = now.strftime("%d-%m-%y %H:%M:%S")
#-------------------------------------
#client = Client(config.API_KEY, config.API_SECRET, tld='com')
client = Client(config.API_KEY, config.API_SECRET)
messenger = Sendline(config.TOKEN_LINE) 


#=== Exmple Percent & Amount ===
#  amount = 0.000234234
#  precision = 5
#  amt_str = "{:0.0{}f}".format(amount, precision)
#-------------------------------
#=== BUY & SELL (Limit/Market) ===  
# order = client.create_order(symbol='BNBBTC',side=SIDE_BUY,type=ORDER_TYPE_LIMIT,timeInForce=TIME_IN_FORCE_GTC,quantity=100,price='0.00001')
#-------------------------------
#=== BUY(Limit/Market) ===   
#def PlaceBUYLimit(amount,symbol)  # order = client.order_limit_buy(symbol='BNBBTC',quantity=100,price='0.00001') 
#def PlaceBUYMarket(amount,symbol)  # order = client.order_market_buy(symbol='BNBBTC',quantity=100)
#-------------------------------
#=== BUY(Limit/Market) === 
#def PlaceSELLLimit(amount,symbol)  # order = client.order_limit_sell(symbol='BNBBTC',quantity=100,price='0.00001')
#def PlaceSELLMarket(amount,symbol) # order = client.order_market_sell(symbol='BNBBTC',quantity=100)
#-------------------------------
def check_trade_coin(conn,coin,data_analysis,last_prices): 
    #data_cmp = coin +'-'+ data_summary["RECOMMENDATION"] +'-'+ str(data_indi["RSI"]) +'-'+ str(data_indi["SMA5"]) +'-'+ str(data_indi["SMA10"]) +'-'+ str(data_indi["SMA20"] )
    sql_str = sql_last_signal_by_coin.replace("#coin#", coin)  
    data = get_single_record(conn,sql_str) 
    if len(data) > 0: 
        #print("1 coin [{}] , recommen [{}] , gauge_buy [{}] , gauge_sell [{}] ,gauge_neutral [{}]".format(coin ,data_analysis.summary["RECOMMENDATION"] , data_analysis.summary["BUY"] , data_analysis.summary["SELL"] ,data_analysis.summary["NEUTRAL"] ) )
        #print("2 coin [{}] , recommen [{}] , gauge_buy [{}] , gauge_sell [{}] ,gauge_neutral [{}]".format(data[0] , data[1] , data[2] ,data[3] ,data[4]) )
        if data[0] == coin and data[1] == data_analysis.summary["RECOMMENDATION"] and data[2] == data_analysis.summary["BUY"] and data[3] == data_analysis.summary["SELL"] and data[4] == data_analysis.summary["NEUTRAL"] :
            return True
        else :
            return False    
    else :
        return False    
    
#-------------------------------
def get_prices(coin): 
    last_prices = {}
    #print("----------------- get_prices : [{}] -----------------".format(coin))
    tickers = client.get_ticker(symbol=coin) 
    last_prices['symbol'] = coin
    last_prices['lastPrice'] = float(tickers['lastPrice'])
    last_prices['askPrice'] = float(tickers['askPrice'])
    last_prices['askQty'] = float(tickers['askQty'])
    return last_prices
    #print ('ราคาล่าสุด  : ' + tickers['lastPrice']) 
    #print ('ราคาขายถูกสุด  : ' + tickers['askPrice'])
    #print ('จำนวนราคาขายถูกสุด  : ' + tickers['askQty'])
#-------------------------------
def inst_trades(conn,coin,last_prices,data_analysis): 
    rec = []
    data = [] 
    #print("----------------- inst_trades : [{}] -----------------".format(coin))
    last_prices = get_prices(coin)  
    rec.append(coin)
    rec.append(data_analysis.summary["RECOMMENDATION"])
    rec.append(data_analysis.summary["BUY"])
    rec.append(data_analysis.summary["SELL"])
    rec.append(data_analysis.summary["NEUTRAL"])
    rec.append(last_prices['lastPrice']) 
    rec.append(data_analysis.indicators["RSI"])
    rec.append(data_analysis.indicators["MACD.macd"])
    rec.append(data_analysis.indicators["MACD.signal"])
    rec.append(data_analysis.indicators["SMA5"])
    rec.append(data_analysis.indicators["SMA10"])
    rec.append(data_analysis.indicators["SMA20"])
    rec.append(data_analysis.indicators["SMA30"])
    rec.append(data_analysis.indicators["SMA50"])
    rec.append(data_analysis.indicators["SMA100"])
    rec.append(data_analysis.indicators["SMA200"])
    rec.append(data_analysis.indicators["EMA5"])
    rec.append(data_analysis.indicators["EMA10"])
    rec.append(data_analysis.indicators["EMA20"])
    rec.append(data_analysis.indicators["EMA30"])
    rec.append(data_analysis.indicators["EMA50"])
    rec.append(data_analysis.indicators["EMA100"])
    rec.append(data_analysis.indicators["EMA200"])
    rec.append(data_analysis.indicators["Pivot.M.Fibonacci.S3"])
    rec.append(data_analysis.indicators["Pivot.M.Fibonacci.S2"])
    rec.append(data_analysis.indicators["Pivot.M.Fibonacci.S1"])        
    rec.append(data_analysis.indicators["Pivot.M.Fibonacci.Middle"])
    rec.append(data_analysis.indicators["Pivot.M.Fibonacci.R1"])
    rec.append(data_analysis.indicators["Pivot.M.Fibonacci.R2"])  
    rec.append(data_analysis.indicators["Pivot.M.Fibonacci.R3"])        
    rec.append("ACTIVE")
    rec.append(str(data_analysis.time)[0:19]) 
    data.append(rec)
    print(data)
    insert_data(conn,sql_inst_signals,data)
#-------------------------------
def send_line(line_info): 
    #line_info['mode'] #  msg , msg_sticker ,image
    #line_info['message']
    #line_info['sticker_id']
    #line_info['package_id']
    #line_info['img_url']
    if (line_info['mode'] == 'msg'):
        messenger.sendtext(line_info['message']) 
    elif(line_info['mode'] == 'msg_sticker'): 
        messenger.sticker(line_info['sticker_id'],line_info['package_id'],line_info['message'])  
    elif(line_info['mode'] == 'image'):    
        messenger.sendimage(line_info['img_url'])
#-------------------------------
#=== Check Signal By coin ===
def SIGNALS_BY_SYMBOL_TDV(coin):
    print("----------------- Start SIGNALS_BY_SYMBOL_TDV : [{}] -----------------".format(coin))
    line_info = {}
    #strongBuy_list = []
    #strongSell_list = []
    data_analysis = []
    data_summary = []
    data_indi = []

    tesla = TA_Handler()
    conn = get_connection()
    #tesla.set_symbol_as(i['symbol'])
    tesla.set_symbol_as(coin)
    tesla.set_exchange_as_crypto_or_stock("BINANCE")
    tesla.set_screener_as_crypto()
    tesla.set_interval_as(Interval.INTERVAL_1_MINUTE)
    #print(i['symbol'])
    #print(coin)
    try:
      data_analysis = tesla.get_analysis()     
    except Exception as e:
      print("No Data")
      #continue 
    data_summary = data_analysis.summary
    data_indi    = data_analysis.indicators
    last_prices  = get_prices(coin) 
 
    if check_trade_coin(conn,coin,data_analysis,last_prices) :
        print("Data Dup") 
    else :    
        if(data_summary["RECOMMENDATION"])=="BUY":
            #inst_trades(conn,coin,"BUY",last_prices,data_indi)
            print("BUY  [{}:{}]  {} , RSI [{}] , Close [{}] , RSI1 [{}] , SMA5 [{}] , SMA10 [{}] , SMA20 [{}] , SMA30 [{}] , SMA100 [{}] ".format(coin ,last_prices['lastPrice'] ,data_summary ,data_indi["RSI"] ,data_indi["close"],data_indi["RSI[1]"],data_indi["SMA5"],data_indi["SMA10"],data_indi["SMA20"],data_indi["SMA50"],data_indi["SMA100"]))  
            inst_trades(conn,coin,last_prices,data_analysis)

        elif(data_summary["RECOMMENDATION"])=="SELL":
            #inst_trades(conn,coin,"SELL",last_prices,data_indi)
            print("SELL  [{}:{}]  {} , RSI [{}] , Close [{}] , RSI1 [{}] , SMA5 [{}] , SMA10 [{}] , SMA20 [{}] , SMA30 [{}] , SMA100 [{}] ".format(coin ,last_prices['lastPrice'] ,data_summary ,data_indi["RSI"] ,data_indi["close"],data_indi["RSI[1]"],data_indi["SMA5"],data_indi["SMA10"],data_indi["SMA20"],data_indi["SMA50"],data_indi["SMA100"]))  
            inst_trades(conn,coin,last_prices,data_analysis)

        elif(data_summary["RECOMMENDATION"])=="STRONG_BUY": 
            print("***** STRONG BUY  [{}:{}]  {} , RSI [{}] , Close [{}] , RSI1 [{}] , SMA5 [{}] , SMA10 [{}] , SMA20 [{}] , SMA30 [{}] , SMA100 [{}] ".format(coin ,last_prices['lastPrice'] ,data_summary ,data_indi["RSI"] ,data_indi["close"],data_indi["RSI[1]"],data_indi["SMA5"],data_indi["SMA10"],data_indi["SMA20"],data_indi["SMA50"],data_indi["SMA100"]))  
            inst_trades(conn,coin,last_prices,data_analysis)
            msg_str = '\n'
            msg_str = msg_str + '-----------------------------------------------------------\n'
            msg_str = msg_str + ' \U0001F4B2  \U0001F49A\U0001F49A\U0001F49A  '+ coin +'  \U0001F49A\U0001F49A\U0001F49A \U0001F4B2  \n'
            msg_str = msg_str + '-----------------------------------------------------------\n'
            msg_str = msg_str + '       \U0001F3AF  จุดเข้า   99.99999    \U0001F3AF \n'
            msg_str = msg_str + '-----------------------------------------------------------\n'
            msg_str = msg_str + ' ราคาล่าสุด   : '+ str(last_prices['lastPrice']) + ' \n'
            msg_str = msg_str + ' SRI              : '+ str(data_indi["RSI"]) + ' \n'
            msg_str = msg_str + ' SMA5         : '+ str(data_indi["SMA5"]) + ' \n'
            msg_str = msg_str + ' SMA10       : '+ str(data_indi["SMA10"]) + ' \n'
            msg_str = msg_str + ' SMA20       : '+ str(data_indi["SMA20"]) + ' \n'
            msg_str = msg_str + ' SMA30       : '+ str(data_indi["SMA30"]) + ' \n'
            msg_str = msg_str + ' SMA100     : '+ str(data_indi["SMA100"]) + ' \n'
            msg_str = msg_str + '-----------------------------------------------------------\n'

            line_info['mode']       = 'msg'  #  msg , msg_sticker ,image
            line_info['message']    =  msg_str #coin +' [' +  str(last_prices['lastPrice']) +  '] :  ตลาดกำลังรุมซื้อ(ขึ้น) หาจังหวะเข้าด่วน!!!!!!'
            #line_info['sticker_id'] =  125
            #line_info['package_id'] =  1
            send_line(line_info)            

        elif(data_summary["RECOMMENDATION"])=="STRONG_SELL": 
            print("***** STRONG SELL  [{}:{}]  {} , RSI [{}] , Close [{}] , RSI1 [{}] , SMA5 [{}] , SMA10 [{}] , SMA20 [{}] , SMA30 [{}] , SMA100 [{}] ".format(coin ,last_prices['lastPrice'] ,data_summary ,data_indi["RSI"] ,data_indi["close"],data_indi["RSI[1]"],data_indi["SMA5"],data_indi["SMA10"],data_indi["SMA20"],data_indi["SMA50"],data_indi["SMA100"]))  
            inst_trades(conn,coin,last_prices,data_analysis)
            msg_str = ' \n'
            msg_str = msg_str + '-----------------------------------------------------------\n' 
            msg_str = msg_str + ' \U0001F4B2  \U00002764\U00002764\U00002764  '+ coin +'  \U00002764\U00002764\U00002764 \U0001F4B2  \n'
            msg_str = msg_str + '-----------------------------------------------------------\n' 
            msg_str = msg_str + '       \U0001F3AF  จุดออก  99.99999    \U0001F3AF \n'
            msg_str = msg_str + '-----------------------------------------------------------\n'
            msg_str = msg_str + ' ราคาล่าสุด   : '+ str(last_prices['lastPrice']) + ' \n'
            msg_str = msg_str + ' SRI              : '+ str(data_indi["RSI"]) + ' \n'
            msg_str = msg_str + ' SMA5         : '+ str(data_indi["SMA5"]) + ' \n'
            msg_str = msg_str + ' SMA10       : '+ str(data_indi["SMA10"]) + ' \n'
            msg_str = msg_str + ' SMA20       : '+ str(data_indi["SMA20"]) + ' \n'
            msg_str = msg_str + ' SMA30       : '+ str(data_indi["SMA30"]) + ' \n'
            msg_str = msg_str + ' SMA100     : '+ str(data_indi["SMA100"]) + ' \n'
            msg_str = msg_str + '-----------------------------------------------------------\n'

            line_info['mode']       = 'msg'  #  msg , msg_sticker ,image
            line_info['message']    =  msg_str #coin +' [' +  str(last_prices['lastPrice']) +  '] :  ตลาดกำลังเทขาย(ลง) หาจังหวะเข้าซื้อด่วน!!!!!!' 
            #line_info['sticker_id'] =  127
            #line_info['package_id'] =  1
            send_line(line_info)        
 
        
 
#************************************************************************
       
def SIGNALS_BY_SYMBOL(coin):
    print("----------------- Start SIGNALS_BY_SYMBOL : [{}] -----------------".format(coin))
    klines = client.get_historical_klines(coin, Client.KLINE_INTERVAL_1MINUTE, "30 minutes ago UTC")
    closes = [float(i[4]) for i in klines] # List Comprehension 
    #print("klines  : [{}] ".format(klines)) 
    closes = np.array(closes)
    #print(closes)

    ema12 = ta.EMA(closes,timeperiod=5)
    ema26 = ta.EMA(closes,timeperiod=10)
    rsi   = ta.RSI(closes,timeperiod=12) 
    #print("rsi  : [{}] ".format(rsi))
    #figure Draw graph
    #fig = plt.figure()
    #axes = fig.add_axes([0.1,0.1,0.8,0.8])
    #axes.set_xlabel("1min time frame")
    #axes.set_ylabel("PRICE {}". format(coin))

    #plot graph
    #plt.plot(closes,"--",color="gray",label="Price")
    #plt.plot(ema12,"-",color="green",label="ema12")
    #plt.plot(ema26,"-",color="red",label="ema24")
    #plt.plot(rsi,"-",color="yellow",label="rsi")

    #cross over / cross under
    crossover  = [] #buy
    crossunder = [] #sell

    for index,val in enumerate(zip(ema12,ema26)) :
        i = val[0]
        j = val[1]
        #print(i , ' , ' , j)
        #cross over  
        if (ema12[index-1] < ema26[index-1]) and (i > j): 
            print("BULLISH Hear FOR {} : {} , {}".format(coin,ema12[index-1]-ema26[index-1],i-j))  
            #BUYH
            #Cal Amount 
            #PlaceBUY
            crossover.append(i)  #จุดที่มีการ cross
            break
        elif (ema12[index-1] > ema26[index-1]) and (i < j):
            print("BEARISH Hear FOR {} : {} , {}".format(coin,ema12[index-1]-ema26[index-1],i-j))              
            #SELL
            #PlaceSELL
            crossunder.append(i) #จุดที่มีการ cross
            break
        else:
             #print("NO SIGNAL FOR {}".format(coin))
             crossover.append(None)  #จุดที่มีการ cross
             crossunder.append(None) #จุดที่มีการ cross
             
            
    crossover = np.array(crossover)
    crossunder = np.array(crossunder)
    
    #if  crossover.size >= 1 :   
    #    print("crossover  : [{}] ".format(crossover))
    #if  crossunder.size >= 1 :       
    #    print("crossunder  : [{}] ".format(crossunder))
    #print(crossover)
    #print(crossunder)

    #plt.plot(crossover,"x",color="green",label="BULLISH")
    #plt.plot(crossunder,"x",color="red",label="BEARISH")

    #plt.legend(loc="upper left")
    #plt.show()
#-------------------------------  


