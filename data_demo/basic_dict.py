#初始化
d={'a':1,2:'b','c':3,4:'d'}
# print(d)
#取长度
print(len(d))
#根据key读写
d['a']=100
print(d)
#添加元素
d['e']=5
print(d)
#删除元素
# del (d['a'])
# print(d)
#判断key是否存在
# if 'a' in d:
#     print('a in d')

# if not ('x' in d):
#     print('x not in d')
# else:
#     print('element in d')

#判断字典是否为空
d={}
if not d:
    print('d in empty')

#遍历
d={'a':1,2:'b','c':3,4:'d'}
print('遍历：')
# for k in d.keys():
#     print(str(k)+': '+str(d[k]))

for k,v in d.items():
    print(str(k)+':'+str(v))

