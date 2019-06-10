import numpy as np
import os

os.chdir("C:/Users/Administrator/Desktop/")
ar=np.random.rand(5,5)
print(ar)
# np.save("test",ar)
# print("finish")

# ar_load=np.load("test.npy")
# print(ar_load)
#存储为文本文档
np.savetxt("savetext.txt",ar,delimiter=',',fmt='%.2f')#%.2f意思是两位小数
print("finish")
ar_loadtxt=np.loadtxt("savetext.txt",delimiter=',')
print(ar_loadtxt)

#生成一个10*10的数组并存储
ar10=np.random.randint(100,size=(10,10))
np.savetxt("100random.txt",ar10,delimiter=',',fmt='%d')#存储为整数
print(ar10)


