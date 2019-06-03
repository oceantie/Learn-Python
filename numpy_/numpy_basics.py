import numpy as np
# a=np.array([1,2,3])
# print(a)
#创建数组
ar1=np.array(range(10))
ar2=np.arange(10)
ar3=np.array([[1,2,3,5],['a','b','c']])
print(ar1)
print(ar2)
print(ar3)
#生成随机数，先生成数字，再生成形状
print(np.random.rand(10).reshape(2,5))

#创建数组arange类似range
print("="*30)
print(np.arange(10))
print(np.arange(10.0))
print(np.arange(5,12))
print(np.arange(5.0,12,2))

#创建数组：linspace:返回在间隔[开始，停止]上计算的num个均匀间隔的样本
print(np.linspace(10,20,num=21,endpoint=True))#10到20分成20份
print(np.linspace(10,13,num=3,endpoint=True))

print("="*30)
print(np.zeros((2,5),dtype=int))
ar4=np.zeros((3,4))
#ones_like（）按照别的数组格式用1进行填充
ar5=np.ones_like(ar4)
print(ar4)
print(ar5)

print(np.eye(3))

#数组形状
ar6=np.arange(10)
ar7=np.zeros((2,5))
print(ar1)
print(ar7)
#T表示转置
print(ar7.T)
#reshape后的元素需要与之前的一样
print(ar6.reshape(2,5))
#resize
print(np.resize(np.arange(10),(2,3)))

#数组复制
ar8=np.arange(10)
# ar9=ar8
ar10=ar8.copy()
ar10[2]=100
# ar8[2]=100
print(ar8,ar10)

#改变数组类型astype
ar11=np.arange(10,dtype=float)
print(ar11.dtype)
print(ar11.astype(np.int64).dtype)

#数组堆叠
# a=np.arange(5)
# b=np.arange(5,9)
# print(a)
# print(b)
#横向连接
# print(np.hstack((a,b)))
print("="*30)

#竖向连接
# a=np.array([[1],[2],[3]])
# b=np.array([['a'],['b'],['c']])
# print(np.vstack((a,b)))

a=np.arange(5)
b=np.arange(5,10)
print(np.stack((a,b),axis=0))

#数组拆分
ar=np.arange(16).reshape(4,4)
print(ar)
#hsplit水平拆分
print(np.hsplit(ar,2)[0])
print(np.vsplit(ar,2)[0])

#运算
ar=np.arange(6).reshape(2,3)
print(ar)
print(ar.mean())#求平均值
print(ar.max())
print(ar.std())#标准差
print(ar.var())#方差
print(ar.sum(),np.sum(ar,axis=0))#求和，axis=0表示按列求和