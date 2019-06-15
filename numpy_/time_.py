import numpy as np
import pandas as pd
import datetime

data1='20170701'
data2=datetime.datetime(2016,10,1,15,0)

t1=pd.Timestamp(data1)
t2=pd.Timestamp(data2)
print(t1,type(t1))
print(t2,type(t2))
print(data2,type(data2))#timestamp直接生成pandas的时间戳，数据类型为pandas的timestamp

#pd.to_datetime多个时间数据转换成时间戳索引
data1='20170701'
data2=datetime.datetime(2016,10,1,15,0)
t1=pd.to_datetime(data1)
t2=pd.to_datetime(data2)
print(t1,type(t1))
print(t2,type(t2))

lst_date=['2017-12-21','2017-12-22','2017-12-23']#时间序列
t3=pd.to_datetime(lst_date)
print(t3,type(t3))#多个时间数据会转换成pandas的DatetimeIndex

data3=['2017-12-21','2017-12-22','2017-12-23','aaaa','2017-2-3']
print(pd.to_datetime(data3,errors='coerce'))#ignore会忽略错误,coerce会把非时间序列的值作为缺失值

#时间序列
#DateTimeIndex TimeSeries
print("="*30)
rng=pd.DatetimeIndex(['12/1/2017','12/2/2017','12/3/2017','12/4/2017','12/5/2017'])
print(rng,type(rng))
print(rng[0],type(rng[0]))
print("="*30)
#直接生成时间索引，支持str，datetime.datetime
#单个时间戳为timestamp，多个时间戳为DatetimeIndex
st=pd.Series(np.random.rand(5),index=rng)
print(st,type(st))
print(st.index)
#以DatetimeIndex为index的Series为TimeSeries，时间序列


#pd.date_range()日期范围：生成日期范围
#2种生成方式：1.start+end;2start/end+periods
#默认频率:day
print("="*30)
rng1=pd.date_range('1/1/2017','1/10/2017',normalize=True)#freq='H'频率为小时
rng2=pd.date_range(start='1/1/2017',periods=10)#period偏移量
rng3=pd.date_range(end='1/30/2017 15:00:00',periods=10)#增加了分时秒

print(rng1,type(rng1))
print(rng2)
print(rng3)
print("="*30)
ran4=pd.date_range(start='1/1/2017 15:00:00',periods=10,name='helloworld')
print(ran4)
print("="*30)
print(pd.date_range('20170101','20170104'))
print(pd.date_range('20170101','20170104',closed='left'))#closed=left表示左边是闭区间
print("="*30)

print(pd.bdate_range('20170101','20170207'))
#pd.bdate_range默认频率为工作日

print(list(pd.date_range(start='1/1/2017',periods=10)))
#直接转化为list，元素未Timestamp

#频率
print("="*30)
print(pd.date_range('2017/1/1','2017/1/4'))#默认freq=D:每个日历日
print(pd.date_range('2017/1/1','2017/1/4',freq='B'))#每个工作日
print(pd.date_range('2017/1/1','2017/1/2',freq='H'))#每个hour
print(pd.date_range('2017/1/1 12:00','2017/1/1 12:10',freq='T'))#T/min
print(pd.date_range('2017/1/1 12:00:00','2017/1/1 12:00:10',freq='S'))#每秒
print(pd.date_range('2017/1/1 12:00:00','2017/1/1 12:00:10',freq='L'))#每豪秒(千分之一秒)
print(pd.date_range('2017/1/1 12:00:00','2017/1/1 12:00:10',freq='U'))#每微秒(百万分之一秒)
print("="*30)
print(pd.date_range('2017/1/1','2017/2/1',freq='W-MON'))#从指定的星期几开始算
print(pd.date_range('2017/1/1','2017/5/1',freq='WOM-2MON'))
#W-2MON:每月的第几个星期几开始算，这里是每月第二个星期一

#pd.date_range()频率2：
print("-"*30)
print(pd.date_range('2017','2018',freq='M'))
print(pd.date_range('2017','2020',freq='Q-DEC'))
print(pd.date_range('2017','2020',freq='A-DEC'))
#M:每月最后一个日历日
#Q-月：指定为月季度末，每个季度末最后一月的最后一个日历日
#A-月:每年指定月份的最后一个日历日

#复合频率
print("-"*30)
print(pd.date_range('2017/1/1','2017/2/1',freq='7D'))#7天
print(pd.date_range('2017/1/1','2017/1/2',freq='2h30min'))#2h30min
print(pd.date_range('2017','2018',freq='2M'))#2月，每月最后一个日历日
print("="*30)

#时间频率转换
ts=pd.Series(np.random.rand(4),index=pd.date_range('20170101','20170104'))
print(ts)
print(ts.asfreq('4H',method='ffill'))
#改变频率，这里是D改为4H
#method:插值格式，None不插值，ffill用之前的值填充，bfill用之后的值填充

#超前和滞后数据
ts=pd.Series(np.random.rand(4),index=pd.date_range('20170101','20170104'))
print(ts)
# print(ts.shift(2))
# print(ts.shift(-2))
print("="*30)
#正数：数值后移
per=ts/ts.shift(1)-1
print(per)