#一维数组
print([i*2 for i in range(10)])
print([i*i for i in range(10)])
print([i*1 for i in range(10) if (i%3)==0])
print([(x,y) for x in range(3) for y in range(3)])
#二维数组
print('二维数组')
a=[[3]*(i+1) for i in range(3)]
print(a)

#乘法问题
print('乘法问题')
a=[[1,2,3]]*3
a[1][1]=100
print(a)

a=[[1,2,3] for i in range(3)]
a[1][1]=100
print(a)
