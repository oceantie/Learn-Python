import numpy as np
import pandas as pd

data={
    "name":['jack','Tom','Mary'],
    'age':[18,19,20],
    'gender':['m','m','f']
}
frame=pd.DataFrame(data)
print(frame)
print(type(frame))

#创建。创建方法：pandas.Dataframe();由数组list组成字典
data1={
    'a': [1, 2, 3],
    'b': [3, 4, 5],
    'c':[5,6,7]
}
data2={
    'one':np.random.rand(3),
    'two':np.random.rand(3)
}
print(data1)
print(data2)
d1=pd.DataFrame(data1,columns=['b','c','a','d'])#colums指定列名，多出的列为空值
d2=pd.DataFrame(data2)
print(d1)
print(d2)

#用serious组成字典
data1={
    'one':pd.Series(np.random.rand(2)),
    'two':pd.Series(np.random.rand(3))#没有设置index的serious
}
data2={
    'one':pd.Series(np.random.rand(2),index=['a','b']),
    'two':pd.Series(np.random.rand(3),index=['a','b','c'])
}
print(data1)#由seris组成的字典创建dataframe，column为字典的key，index为seris的标签
print(data2)
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
print(df1)
print(df2)

#通过二维数组直接创建
ar=np.random.rand(9).reshape(3,3)
print(ar)
df1=pd.DataFrame(ar)
df2=pd.DataFrame(ar,index=['a','b','c'],columns=['one','two','three'])
print(df1)
print(df2)

#由字典组成的列表创建
print('由字典组成的列表创建')
data=[{ 'one':1,'two':2},{'one':5,'two':10,'three':20}]
print(data)
df1=pd.DataFrame(data)
df2=pd.DataFrame(data,index=['a','b'])
df3=pd.DataFrame(data,columns=['one','two'])
print(df1)
print(df2)
print(df3)

#有字典组成的字典
data={
    'jack':{'math':90,'english':89,'art':78},
    'marry':{'math':80,'english':81,'art':72},
    'tom':{'math':94,'english':83,'art':73},
}
df1=pd.DataFrame(data)
print(df1)
df2=pd.DataFrame(data,columns=['jack','tom','bob'])
df3=pd.DataFrame(data,index=['a','b','c'])
print(df2)
print(df3)