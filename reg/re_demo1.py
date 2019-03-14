import re

# text="hello"
# #match从开始匹配
# ret=re.match("he",text)
# print(ret.group())

# . 点是匹配任意字符
# text="hello"
# ret=re.match(".",text)
# print(ret.group())

#\d匹配任意number(0-9)
# text="1e123lo"
# ret=re.match("\d+",text)
# print(ret.group())

#\D匹配任意非number
# text="e123lo"
# ret=re.match("\D+",text)
# print(ret.group())

#匹配空白字符（\s）
# text=" "
# ret=re.match('\s',text)
# print(ret.group())

#\w匹配a-z,A-Z以及数字
# text='a12213'
# ret=re.match('\w',text)
# print(ret.group())
#W和小写w相反

#组合方式，只要满足中括号中的字符，就可以匹配
# text="a11"
# ret=re.match('[a]',text)
# print(ret.group())

# text="010-234214124"
# ret=re.match("[\d\-]+",text)
# print(ret.group())

#中括号形式替代\D
# text="a"
# ret=re.match('[^0-9]',text)
# print(ret.group())

# *匹配0或者任意个字符
# text="123213"
# ret=re.match("\d*",text)
# print(ret.group())

# +匹配一个或者多个字符，至少一个
# text="asdada123213"
# ret=re.match("\w+",text)
# print(ret.group())

# ?匹配一个或者0个，要么没有要么一个
# text="asdada123213"
# ret=re.match("\w?",text)
# print(ret.group())

# {m}匹配m个字符
# text="abed"
# ret=re.match("\w{2}",text)
# print(ret.group())

# {m,n}匹配m-n个字符
text="ab_d"
ret=re.match("\w{1,3}",text)
print(ret.group())