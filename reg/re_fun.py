import re

#find_all函数：找出所有满足条件的，返回一个列表
text="apple's price $99,orange's price is $10"
ret=re.findall("\$\d+",text)
print(ret)

#sub用来替换匹配到满足条件的字符串
text="apple's price $99,orange's price is $10"
ret=re.sub("\$\d+","0",text)
print(ret)

text="""
<li class="hcrowd4">
<a href="/wl/csgz/">
<strong>高薪专区</strong>
<p>毕业拿高薪并不难</p>
</a>
</li>
"""

ret=re.sub("<.+?>","",text)
print(ret)

#split()：使用正则的方式，分割字符串
text="hello$world ni hao"
ret=re.split("[^a-zA-Z]",text)#只要不是英文的都进行分割
print(ret)

#compile：正则执行次数较多，使用compile先编译存放在内存以提升效率;传入flag，可以写注释
text="the number is 11.1"
r=re.compile(r"""
    \d+  #小数点前面的数字
    \.?#小数点本身
    \d*#小数点后面的数字
""",re.VERBOSE)
ret=re.search(r,text)
print(ret.group())
