li1=[1,2,3,4]
li2=[]
#append添加的是数组，extend是单独添加的各个元素
# li1.append([5,6])
# li1.extend([5,6])
# print(li1)
#pop是直接删除最后一个元素，del删除索引元素
# li1.pop()
# del(li1[2])
# print(li1)
#判断元素是否存在
# print(1 in li1)
# print(7 in li1)
#列表是否为空
# if not li2:
#     print('empty')

#字符串,改变字符串的值
# s='abcdefg'
# li=list(s)
#
# li[4]='E'
# s=''.join(li)
# print(s)

#遍历
# li=[1,2,3]
# for i in li:
#     print(i)

for i in range(len(li1)):
    print(li1[i])
