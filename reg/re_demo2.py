import re

#手机号验证,以1开头，第二位可以是34587
text='18575651587'
ret=re.match('1[34587]\d{9}',text)
print(ret.group())

#邮箱验证,用户名可以是数字、下划线字母然后是@，然后是域名
text='hover12_@qq.com'
ret=re.match('\w+@[a-z0-9]+\.[a-z]+',text)
print(ret.group())

#验证url：URL的规则是前面是http或者https或者是ftp然后加上冒号，再加上斜杠，在后面就是任意非空白字符
text='http://www.baidu.com'
ret=re.match("(http|https|ftp)://[^\s]+",text)
print(ret.group())

#验证身份证：总共有18位，前17位是数字，最后一位可以是数字，也可以是小写x或者大写X
text='510703199108231213'
ret=re.match("\d{17}[\dxX]",text)
print(ret.group())

# ^(脱字号)表示以。。开始,如果在中括号总表示取反
text='hello'
ret=re.search("^h",text)
print(ret.group())

#  $符号表示以。。结尾
text='xxx@163.com'
ret=re.search("\w+@163.com$",text)
print(ret.group())

# |符号表示匹配多个字符后者表达式

#贪婪模式和非贪婪模式,默认为贪婪模式,?为非贪婪模式
text='0123456'
ret=re.match("\d+?",text)
print(ret.group())

text='<h1>标题</h1>'
ret=re.match("<.+?>",text)
print(ret.group())


#匹配0-100之间的数字
# 可以出现 1 2 3 4 10
# 不可以出现 09 101
#要么为一位，要么为两位，要么为100
text='100'
ret=re.match("[1-9]\d?$|100$",text)
print(ret.group())

#\转义字符
text="apple price is $299"
ret=re.search("\$\d+",text)
print(ret.group())
#加r就代表原生字符串。
# text=r"\n"
# print(text)

text="\\c"#=\c
ret=re.match(r"\\c",text)
print(ret.group())

#分组:group(1)里的标识第一个圆括号匹配到的类容;还可以传多个参数
text="apple's price $99,orange's price is $10"
ret=re.search(".*(\$\d+).*(\$\d+)",text)
print(ret.group(1,2))
#所有的子分组都拿出来
print(ret.groups())




