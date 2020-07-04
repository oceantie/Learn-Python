import pandas as pd
import numpy as np
import tushare as ts
import csv
import time

stocks=[]
ts.set_token('c2ce9df72eb324c01e809da43379650bbc25f3a0f0c2ef9aa75f6baa')
pro = ts.pro_api()

# print(data_2)
#print(df.loc[df["change"]>0])#上涨的日子
# print(df)
# data=df["change"]
# print(data_2.iloc[2])
#
# df = pro.daily(ts_code='000801.SZ', start_date='20200501', end_date='20200702')
# data_2 = df.iloc[:, [0, 1, 7]]

def get_data(ts_code,start_date,end_date,retry_count,pause):#请求数据
    # print(ts_code)
    for x in range(retry_count):
        try:
            df = pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
        except:
            time.sleep(pause)
        else:
            singal_stockcan(df)
            break

def singal_stockcan(df):#请求到的每只股票数据分析
    data_2 = df.iloc[:, [0, 1, 7]]
    # print(data_2)
    for index,x in enumerate(data_2["change"]):#如果涨幅为正则算作阳线
        if 7+index<=len(data_2):
            #if data_2["change"].at[index]>0 and data_2["change"].at[index+1]>0 and data_2["change"].at[index+2]>0 and data_2["change"].at[index+3]>0 and data_2["change"].at[index+4]>0:
            if data_2["change"].at[index]>0 and data_2["change"].at[index+1]>0 and data_2["change"].at[index+2]>0 and data_2["change"].at[index+3]>0 and data_2["change"].at[index+4]>0 and data_2["change"].at[index+5]>0 and data_2["change"].at[index+6]>0:
                # print(data_2.iloc[index])
                data_all = {
                    'code': data_2.iloc[index]['ts_code'],
                    'date': data_2.iloc[index]["trade_date"]
                }
                write_csv(data_all)#获取到七连阳股票数据
        else:
            break

def get_allstock(stock_count):#获取需要查找的股票代码
    stock_data = pro.query('stock_basic', exchange='', list_status='L',
                           fields='ts_code,symbol,name,area,industry,list_date')
    stock_num=stock_data.head(stock_count)["ts_code"]
    for x in stock_num:
        stocks.append(x)

def stock_list(stock_count,start_date,end_date):#遍历需要爬取的股票代码
    get_allstock(stock_count)
    for each_stock in stocks:
        get_data(each_stock,start_date,end_date,3,2)

def write_csv(stock_data):#数据内容写入csv
   heade=['code','date']
   with open('stock.csv', 'a', newline='',encoding='utf-8')as f:
       writer = csv.DictWriter(f, heade)
       writer.writerow(stock_data)
       print(stock_data)
       print("=================")

if __name__ == '__main__':
    stock_list(3000,"20200101","20200704")




