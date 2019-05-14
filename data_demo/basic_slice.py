li=[0,1,2,3,4,5,6,7,8,9,10]
#切片
print(li[2:5])
print(li[:4])
print(li[5:])
print(li[:])
print(li[0:6:2])#第三个参数是步长
print(li[3::2])

#负索引
print('负索引')
print(li[::-1])
print(li[::-2])
print(li[-6:-1:1])
print(li[-1::-1])