import numpy as np
import pandas as pd

ar=np.random.rand(5)
s=pd.Series(ar,index=list('abcde'))#serious相比于ndarry是一个自带索引index的数组，相当于一维数组加索引
print(ar)
print(s)
print(type(s))
print("-"*30)
print(s.index)
print(s.values)

#创建serious，由字典创建
dic={'a':1,'b':2,'c':3}
s2=pd.Series(dic)
print(s2)

#通过一维数组创建
arr=np.random.rand(10)
s=pd.Series(arr,index=list('abcdefghij'))
print(s)

#通过标量创建
s=pd.Series(100,index=range(10))
print(s)

dic2={'jack':90,'marry':100,'top':22}
s3=pd.Series(dic2,name='task')
print(s3)

#下标索引
# s=pd.Series(np.random.rand(10))
# print(s)
# print(s[5])
#标签索引
s=pd.Series(np.random.rand(5),index=['a','b','c','d','e'])
print(s)
print(s['a'])
print(s[['a','b']])#选取多个标签要用两个中括号
#切片
print("切片")
print(s[1:4],s[4])#下标切片
print(s['a':'c'])#标签切片

#布尔型索引s
print("="*30)
s=pd.Series(np.random.rand(3)*100)
s[4]=None#添加一个空值
print(s)
bs1=s>50
bs2=s.isnull()
bs3=s.notnull()
print(bs1,type(bs1),bs1.dtype)
print(bs2)
print(bs3,type(bs3),bs3.dtype)