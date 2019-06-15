import numpy as np
import pandas as pd

df=pd.DataFrame(np.random.rand(16).reshape(4,4)*100,columns=['a','b','c','d'])
print(df)
df['e']=10#新增列
df.loc[4]=20#新增行
print(df)
df.iloc[::2]=101#每隔两行改变值
print(df)
# df[['a','c']]=100#更改两列的值
# print(df)

#删除
print('删除')
print(df)
del df['a']#del删除列
print(df)
# print(df.drop([1,2]))#drop删除行，inplace=False删除后不改变源数据
print(df.drop(['b'],axis=1))#如果要删除列，需要加上axis=1
print(df)

#对齐
df1=pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df2=pd.DataFrame(np.random.rand(7,3),columns=['a','b','c'])
print(df1)
print(df2)
print("-----")
print(df1+df2)#两个数组相加

#排序，同样适用series
df3=pd.DataFrame(np.random.rand(16).reshape(4,4)*100,columns=['a','b','c','d'])
print(df3)
print(df3.sort_values(['a'],ascending=True))#升序
print(df3.sort_values(['a'],ascending=False))#降序

df4=pd.DataFrame(
    {
        'a':[1,1,1,1,2,2,2,2],
        'b':list(range(8)),
        'c':list(range(8,0,-1))
    }
)
print(df4)
print(df4.sort_values(['a','c']))#多列排序，按照列顺序排序

#按索引排序
df5=pd.DataFrame(np.random.rand(16).reshape(4,4)*100,index=[5,4,3,2],columns=['a','b','c','d'])
df6=pd.DataFrame(np.random.rand(16).reshape(4,4)*100,index=['h','s','x','g'],columns=['a','b','c','d'])
print(df5)
print(df5.sort_index())#按照index排序
print(df6)
print(df6.sort_index())#按照index排序
