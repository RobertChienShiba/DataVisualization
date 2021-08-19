# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 01:20:26 2021
@author: rober
adapted from sentdex Matplotlib Tutorial
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
from matplotlib import style

import numpy as np
import datetime as dt
import pandas as pd
import pandas_datareader as pdr
import requests

style.use('fivethirtyeight')

def moving_average(data,period):
    return data['Close'].rolling(period).mean()

def high_minus_low(highs, lows):
    return highs-lows


  
def get_data(stock_number):
    headers = {"Accept": "application/json",
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                "Accept-Encoding": "none",
                "Accept-Language": "en-US,en;q = 0.8",
                "Connection": "keep-alive",
                "Referer": "https://cssspritegenerator.com",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML,like Gecko) Chrome / 23.0.1271.64Safari / 537.11"
               }    
    with requests.Session() as s:
        s.headers = headers
    start_dt=input("請輸入開始日期(格式:Y/M/D):")
    end_dt=input("請輸入結束日期(格式:Y/M/D):")
    #start = dt.datetime(2021, 1, 1)
    start = dt.datetime.strptime(start_dt,"%Y/%m/%d")
    end =  dt.datetime.strptime(end_dt,"%Y/%m/%d")
    df= pdr.DataReader(stock_number, 'yahoo', start=start, end=end,session=s,pause=1)
    df.index = mdates.date2num(df.index)
    return df

def graph_data(stock):
    fig = plt.figure(facecolor='white',figsize=(15,10))
    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1,facecolor="w")
    plt.title(stock)
    plt.ylabel('H-L')
    ax2 = plt.subplot2grid((6,1), (1,0), rowspan=4, colspan=1, sharex=ax1,facecolor="w")
    plt.ylabel('Price')
    ax2v = ax2.twinx()
    
    ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1,facecolor="w")
    plt.ylabel('MAvgs')
    
    try:
        data=get_data(stock)
    except :
        print("爬蟲程式出現錯誤或您輸入的股票代碼有誤")
        return 
    date=data.index
    Open=data["Open"].values
    data.drop(["Open","Adj Close"],axis="columns",inplace=True)
    data.insert(0,"Date",date)
    data.insert(1,"Open",Open)
    ma1 = moving_average(data,MA1)
    ma2 = moving_average(data,MA2)
    start = len(date[max(MA2,MA1)-1:])
    h_l = list(map(high_minus_low, data["High"], data["Low"]))
    

    ax1.plot_date(date[-start:],h_l[-start:],'-', label='H-L')
    ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='lower'))

    candlestick_ohlc(ax2, data.values[-start:], width=0.6,colorup='#db3f3f',colordown='green',alpha=.4)
    

    ax2.yaxis.set_major_locator(mticker.MaxNLocator(nbins=7, prune='upper'))
    ax2.grid(True)
    
    bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
    
    ax2.annotate(str(round(data["Close"].values[-1],2)), (date[-1], data["Close"].values[-1]),
                 bbox=bbox_props,ha="left",va="center",
                 xytext = (60,0),textcoords="offset points")
    

##    # Annotation example with arrow
##    ax2.annotate('Bad News!',(date[11],highp[11]),
##                 xytext=(0.8, 0.9), textcoords='axes fraction',
##                 arrowprops = dict(facecolor='grey',color='grey'))
##
##    
##    # Font dict example
##    font_dict = {'family':'serif',
##                 'color':'darkred',
##                 'size':15}
##    # Hard coded text 
##    ax2.text(date[10], closep[1],'Text Example', fontdict=font_dict)

    ax2v.plot([],[], color='#0079a3', alpha=0.4, label='Volume')
    ax2v.fill_between(data["Date"].values[-start:],0, data["Volume"].values[-start:], facecolor='#0079a3', alpha=0.4)
    #ax2v.axes.yaxis.set_ticklabels([])
    ax2v.set_yticklabels([])
    ax2v.grid(False)
    ax2v.set_ylim(0, 3*data["Volume"].max())



    ax3.plot(date[-start:], ma1.values[-start:], linewidth=1, label=(str(MA1)+'MA'))
    ax3.plot(date[-start:], ma2.values[-start:], linewidth=1, label=(str(MA2)+'MA'))
    
    ax3.fill_between(date[-start:], ma2.values[-start:], ma1.values[-start:],
                     where=(ma1.values[-start:] < ma2.values[-start:]),
                     facecolor='g', edgecolor='g', alpha=0.5,interpolate=True)

    ax3.fill_between(date[-start:], ma1.values[-start:], ma2.values[-start:],
                     where=(ma1.values[-start:] > ma2.values[-start:]),
                     facecolor='r', edgecolor='r', alpha=0.5,interpolate=True)
    
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax3.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax3.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='upper'))

    # for label in ax3.xaxis.get_ticklabels():
    #     label.set_rotation(45)
    plt.xticks(rotation=15)


    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.subplots_adjust(left=0.1, bottom=0.15, right=0.95, top=0.95, wspace=.2, hspace=0)

    ax1.legend(loc=9,prop={'size':11},frameon=False)
    # leg = ax1.legend(loc=9, ncol=2,prop={'size':11})
    # leg.get_frame().set_alpha(0.4)
    
    ax2v.legend(loc=9,prop={'size':11},frameon=False)
    # leg = ax2v.legend(loc=9, ncol=2,prop={'size':11})
    # leg.get_frame().set_alpha(0.4)
    
    ax3.legend(loc=9,prop={'size':11},frameon=False)
    # leg = ax3.legend(loc=9, ncol=2,prop={'size':11})
    # leg.get_frame().set_alpha(0.4)
    plt.tight_layout()
    plt.show()
    #fig.savefig('google.png',bbox_inches='tight')
while True:
    company=input("請輸入股票編碼(台灣公司請在後方加入.TW)(-1->離開 0->重新輸入):")
    if company == "0" :
        continue
    elif company == "-1":
        break
    try:
        MA1 = int(input("請輸入移動平均線天數(-1->離開 0->重新輸入):"))
        MA2 = int(input("請輸入移動平均線天數(-1->離開 0->重新輸入):"))
    except ValueError as e:
        print("你輸入的不是數字!")
        print("請重新輸入")
        continue
    if MA1 == 0 :
        continue
    elif MA1 == -1:
        break
    if MA2 == 0 :
        continue
    elif MA2 == -1:
        break
    graph_data(company.upper())
    
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import dates as mdates
# from matplotlib import ticker as mticker
# from mpl_finance import candlestick_ohlc
# from matplotlib.dates import DateFormatter
# import datetime as dt

# # 匯入資料，把csv檔(連結下方)放到與程式檔同一資料夾
# df = pd.read_csv(r'C:\Users\rober\Desktop\python visual\file.csv',parse_dates=["Date"],index_col=0).dropna()
# df = df[(df.index > '2018-06-01')]
# df_plot = df


# #計算MA線
# def moving_average(data,period):
#     return data['Close'].rolling(period).mean()

# #計算KD線
# '''
# Step1:計算RSV:(今日收盤價-最近9天的最低價)/(最近9天的最高價-最近9天的最低價)
# Step2:計算K: K = 2/3 X (昨日K值) + 1/3 X (今日RSV)
# Step3:計算D: D = 2/3 X (昨日D值) + 1/3 X (今日K值)
# '''
# def KD(data):
#     data_df = data.copy()
#     data_df['min'] = data_df['Low'].rolling(9).min()
#     data_df['max'] = data_df['High'].rolling(9).max()
#     data_df['RSV'] = (data_df['Close'] - data_df['min'])/(data_df['max'] - data_df['min'])
#     data_df = data_df.dropna()
#     # 計算K
#     # K的初始值定為50
#     K_list = [50]
#     for num,rsv in enumerate(list(data_df['RSV'])):
#         K_yestarday = K_list[num]
#         K_today = 2/3 * K_yestarday + 1/3 * rsv
#         K_list.append(K_today)
#     data_df['K'] = K_list[1:]
#     # 計算D
#     # D的初始值定為50
#     D_list = [50]
#     for num,K in enumerate(list(data_df['K'])):
#         D_yestarday = D_list[num]
#         D_today = 2/3 * D_yestarday + 1/3 * K
#         D_list.append(D_today)
#     data_df['D'] = D_list[1:]
#     use_df = pd.merge(data,data_df[['K','D']],left_index=True,right_index=True,how='left')
#     return use_df

# def prepare_data(data):
#     data_df = data.copy()
#     data_df['DateTime'] = data_df.index
#     data_df = data_df.reset_index()
#     data_df = data_df[['DateTime','Open','High','Low','Close',"Volume","Adj Close"]]
#     data_df['DateTime'] = mdates.date2num(data_df['DateTime'])
#     return data_df

# # 畫股價圖
# # 顏色:https://matplotlib.org/users/colors.html
 
# #畫股價線圖與蠟燭圖
# def plot_stock_price(data):
#     Ma_10 = moving_average(data,10)
#     Ma_50 = moving_average(data,50)
#     Length = len(data['DateTime'].values[50-1:])
#     fig = plt.figure(facecolor='white',figsize=(15,10))
#     ax1 = plt.subplot2grid((6,4), (0,0),rowspan=4, colspan=4, facecolor='w')
#     candlestick_ohlc(ax1, data.values[-Length:],width=0.6,colorup='red',colordown='green')
#     Label1 = '10 MA Line'
#     Label2 = '50 MA Line'
#     ax1.plot(data.DateTime.values[-Length:],Ma_10[-Length:],'black',label=Label1, linewidth=1.5)
#     ax1.plot(data.DateTime.values[-Length:],Ma_50[-Length:],'navy',label=Label2, linewidth=1.5)
#     ax1.legend(loc=9,prop={'size':11},frameon=False)
#     ax1.grid(True, color='black')
#     ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
#     ax1.yaxis.label.set_color("black")
#     ax1.tick_params(axis='y', colors='black')
#     ax1.tick_params(axis='x', colors='black')
#     plt.ylabel('Stock price and Volume')
#     plt.suptitle('Stock Code:2330',color='black',fontsize=16)
#     #畫交易量
#     ax1v = ax1.twinx()
#     ax1v.fill_between(data.DateTime.values[-Length:],0, df.Volume.values[-Length:], facecolor='navy', alpha=.4)
#     ax1v.axes.yaxis.set_ticklabels([])
#     ax1v.grid(False)
#     ax1v.set_ylim(0, 3*df.Volume.values.max())
#     ax1v.tick_params(axis='x', colors='black')
#     ax1v.tick_params(axis='y', colors='black')
#     #加入KD線在下方
#     df_kd=KD(data)
#     ax2 = plt.subplot2grid((6,4), (4,0), sharex=ax1, rowspan=2, colspan=4, facecolor='white')
#     ax2.plot(data.DateTime.values[-Length:], df_kd.K[-Length:],color='#db3f3f', linewidth=1.5,label="K")
#     ax2.plot(data.DateTime.values[-Length:], df_kd.D[-Length:],color='#77d879', linewidth=1.5,label="D")
#     ax2.fill_between(data.DateTime.values[-Length:], df_kd["K"].values[-Length:],
#                      df_kd.D.values[-Length:],
#                      where=(df_kd.K.values[-Length:]>df_kd.D.values[-Length:]),
#                      color='#db3f3f',interpolate=True,alpha=0.4,edgecolor='#db3f3f')
#     ax2.fill_between(data.DateTime.values[-Length:], df_kd.K.values[-Length:],
#                  df_kd.D.values[-Length:],
#                  where=(df_kd.K.values[-Length:]<df_kd.D.values[-Length:]),
#                  color='#77d879',interpolate=True,alpha=0.4,edgecolor='#77d879')
#     ax2.plot([],[],label="Gain",color='#db3f3f',alpha=.4)
#     ax2.plot([],[],label="Loss",color='#77d879',alpha=.4)
#     ax2.legend(loc="lower right",prop={'size':11},frameon=False,labelspacing=0.2)
#     plt.ylabel('KD Value', color='black')
#     ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    
#     plt.setp(ax1.get_xticklabels(), visible=False)
#     plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=.2, hspace=0)
#     plt.tight_layout()
#     fig.autofmt_xdate(bottom=.1,rotation=15,ha="center")
#     plt.show()

# daysreshape = prepare_data(df_plot)
# plot_stock_price(daysreshape)
# plt.show()
