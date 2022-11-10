from py5paisa import FivePaisaClient
import talib as tl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ta
from datetime import datetime
op_pr=[]
cl_pr=[]
op_prs=[]
cl_prs=[]
profit_list=[]
# def current_timee():
#    now=datetime.now()
#    current_time=now.strftime("%H:%M")
#    return current_time
while True:
    #print(current_timee())
    if datetime.now().strftime("%H:%M") == '9:15':
        cred={
            "APP_NAME":"",
            "APP_SOURCE":"",
            "USER_ID":"",
            "PASSWORD":"",
            "USER_KEY":"",
            "ENCRYPTION_KEY":""
            }

        client = FivePaisaClient(email="", passwd="", dob="",cred=cred)
        client.login()
        while True:
            if datetime.now().strftime("%H:%M") != "15:25":
                
                while True:
                    if datetime.now().minute%5==0 and datetime.now().second == 00:
                        df=client.historical_data('N','C',5900,'5m','2022-07-09','2022-11-1')
                        print(df)
                        close=df['Close']
                        high=df['High']
                        low=df['Low']
                        vol=df['Volume']
                        tst=df['Datetime']
                        bb=tl.BBANDS(close,20,2,2,0)
                        vwap=ta.volume.VolumeWeightedAveragePrice(high=df['High'], 
                        low=df['Low'], close=df['Close'], volume=df['Volume'],
                        window=20).volume_weighted_average_price()
                        rsi=tl.RSI(close,14)
                        x=len(close)-1
                        print(x)
                        m=x
                        flip=15
                        flip0=100
                        for j in range(15):                                             
                            if close[x] > vwap[x]:
                                flip=flip+0
                            else:
                                flip=flip-1
                            if close[x] < vwap[x]:
                                flip0=flip0+0
                            else:
                                flip0=flip0-1
                            x=x-1
                        if flip == 15 and (bb[2][m]*(1+0.005)) >= low[m]:
                            op_pr.append(close[m])
                            while True:
                                if datetime.now().minute %5==0:
                                    df1=client.historical_data('N','C',5900,'5m','2022-07-09','2022-11-1')
                                    close1=df1['Close']
                                    high1=df1['High']
                                    low1=df1['Low']
                                    vol1=df1['volume']
                                    bb1=tl.BBANDS(close,20,2,2,0)
                                    x1=len(high1)-1
                                    if bb1[0][x1] < high1[x1]:
                                        cl_pr.append(close[x1])
                                        break
                        elif flip0 == 100 and (bb[0][m]*(1+0.005)) <= high[m]:
                            op_prs.append(close[m])
                            while True:
                                if datetime.now().minute %5==0:
                                    df1=client.historical_data('N','C',5900,'5m','2022-07-09','2022-11-1')
                                    close1=df1['Close']
                                    high1=df1['High']
                                    low1=df1['Low']
                                    vol1=df1['volume']
                                    bb1=tl.BBANDS(close,20,2,2,0)
                                    x1=len(high1)-1
                                    if bb1[2][x1] > low[x1]:
                                        cl_prs.append(close[x1])
                                        break
                            
                
            elif datetime.now().strftime("%H:%M") == "15:30":
                for i in range(len(cl_pr)):
                    profit_v=cl_pr[i]-cl_pr[i]
                    profit_list.append(profit_v)
                    print(sum(profit_list))
                print("done with scanning for siganls,back to scanning 9:15")
                break
    
        
            