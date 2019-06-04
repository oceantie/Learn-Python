import numpy as np

#一维数组切片和python数组一样
ar1=np.arange(10)
print(ar1)
print(ar1[:3])
print(ar1[::2])

#二维数组
ar2=np.arange(16).reshape(4,4)
print(ar2)
print(ar2[2])
print(ar2[2][2])
print(ar2[1:3])
print(ar2[2,2])
print(ar2[:1,2:])

#三维数组
print('='*30)
ar3=np.arange(12).reshape(3,2,2)
print(ar3)
print(ar3[1][0])#表示第二个二维数组的第一组数据

#布尔型切片
print("="*30)
ar4=np.arange(12).reshape(3,4)
i=np.array([True,False,True])
j=np.array([True,True,False,False])
print(ar4)
print(ar4[i,:])#第一个参数为行，因为是布尔值第0个和第2个为true所以选取第0行和第2行
print(ar4>5)#得到数组的布尔值
print(ar4[ar4>5])#得到大于5的数组值

#随机数
samples=np.random.normal(size=(4,4))#normal表示标准正态分布样本值
print(samples)

a=np.random.rand()#rand（）生成一个0-1的随机浮点数
print(a)
print(np.random.rand(3))#生成1维数组
print(np.random.rand(2,4))##生成2维数组

data1=np.random.rand(500)
data2=np.random.rand(500)
data3=np.random.randn(1000)#正态分布
data4=np.random.randn(1000)

import matplotlib.pyplot as plt

# plt.scatter(data1,data2)
# plt.scatter(data3,data4)
# plt.show()

print(np.random.randint(1,5))#取一个1到5的整数
print(np.random.randint(10,size=10))#指定size产生随机数
print(np.random.randint(10,size=(2,5)))#指定行列数，产生2维数组
