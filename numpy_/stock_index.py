import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tushare as ts
ts.set_token('c2ce9df72eb324c01e809da43379650bbc25f3a0f0c2ef9aa75f6baa')
#获取数据
s_pf='600848'
s_gd='601818'
sdate='2016-01-01'
edate='2016-12-31'
pro=ts.pro_api()
#print(ts.get_hist_data('600848')) #一次性获取全部日k线数据
# res=ts.pro_bar(ts_code='000001.SZ', adj='qfq', start_date='20180101', end_date='20181011')
# print(res.close)

df_pf=ts.pro_bar(ts_code='002407.SZ', adj='qfq', start_date='20180101', end_date='20190521').sort_index(axis=0,ascending=True)
df_gd=ts.pro_bar(ts_code='002092.SZ', adj='qfq', start_date='20190101', end_date='20190521').sort_index(axis=0,ascending=True)

# df_pf=ts.get_h_data(s_pf,start=sdate,end=edate)
# df_gd=ts.get_h_data(s_gd,start=sdate,end=edate).sort_index(axis=0,ascending=True)
# print(df_pf.close)
#df=pd.concat([df_pf.close,df_gd.close],axis=1,keys=['pf_close','gd_close'])
df=pd.concat([df_pf.close],axis=1,keys=['pf_close'])
df.ffill(axis=0,inplace=True)#填充数据
df.to_csv('pf_gd.csv')

corr=df.corr(method='pearson',min_periods=1)
df.plot(figsize=(30,18))
plt.savefig('pf_gd.png')
plt.close()