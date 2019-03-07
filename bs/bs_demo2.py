from bs4 import BeautifulSoup

html="""
<table class="tablelist" cellpadding="0" cellspacing="0">
		    	<tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48290&keywords=&tid=0&lid=2268">26699-智慧零售产品运营（深圳/成都）（成都）</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>成都</td>
					<td>2019-03-07</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48003&keywords=&tid=0&lid=2268">22989-腾讯云设计中心-高级交互设计师（成都）</a></td>
					<td>设计类</td>
					<td>1</td>
					<td>成都</td>
					<td>2019-03-07</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47951&keywords=&tid=0&lid=2268">HY6-互娱市场策划与推广(成都)</a></td>
					<td>市场类</td>
					<td>1</td>
					<td>成都</td>
					<td>2019-03-07</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47775&keywords=&tid=0&lid=2268">25666-西南区域川藏拓展组泛企业线组长</a></td>
					<td>市场类</td>
					<td>1</td>
					<td>成都</td>
					<td>2019-03-07</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47684&keywords=&tid=0&lid=2268">15575-《王者荣耀》后台开发高级工程师（成都）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>成都</td>
					<td>2019-03-07</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47634&keywords=&tid=0&lid=2268">18924-行政秘书（成都）</a></td>
					<td>职能类</td>
					<td>1</td>
					<td>成都</td>
					<td>2019-03-07</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47560&keywords=&tid=0&lid=2268">25927-游戏高级测试工程师（成都）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>成都</td>
					<td>2019-03-07</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47536&keywords=&tid=0&lid=2268">15575-《QQ三国》商业化活动运营（成都）</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>成都</td>
					<td>2019-03-07</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47471&keywords=&tid=0&lid=2268">PCG10-高级产品经理（工具产品方向）</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>成都</td>
					<td>2019-03-07</td>
		    	</tr>
		    			    	<tr class="odd test" id="test">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47380&keywords=&tid=0&lid=2268">22989-腾讯云serverless运营开发工程师（成都）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>成都</td>
					<td>2019-03-07</td>
		    	</tr>
		    			    	<tr class="f" id="test">
		    		<td colspan="5">
		    			<div class="left">共<span class="lightblue total">67</span>个职位</div>
		    			<div class="right"><div class="pagenav"><a href="javascript:;" class="noactive" id="prev">上一页</a><a class="active" href="javascript:;">1</a><a href="position.php?lid=2268&tid=&keywords=请输入关键词&start=10#a">2</a><a href="position.php?lid=2268&tid=&keywords=请输入关键词&start=20#a">3</a><a href="position.php?lid=2268&tid=&keywords=请输入关键词&start=30#a">4</a><a href="position.php?lid=2268&tid=&keywords=请输入关键词&start=40#a">5</a><a href="position.php?lid=2268&tid=&keywords=请输入关键词&start=50#a">6</a><a href="position.php?lid=2268&tid=&keywords=请输入关键词&start=60#a">7</a><a href="position.php?lid=2268&tid=&keywords=请输入关键词&start=10#a" id="next">下一页</a><div class="clr"></div></div></div>
		    			<div class="clr"></div>
		    		</td>
		    	</tr>
		    </table>

"""
soup=BeautifulSoup(html,'lxml')
#获取所有的tr标签
# trs=soup.find_all('tr')
# for tr in trs:
#     print(tr)
#     print("="*30)
#     print(type(tr))
#     break
#获取第二个tr标签,在列表层面选取
# trs=soup.find_all('tr',limit=2)[1]
# print(trs)

#获取class为even的标签
#trs=soup.find_all('tr',class_='even')
# trs=soup.find_all('tr',attrs={'class':"even"})
# for tr in trs:
#     print(tr)


#获取id等于test和class为test的标签
#trs=soup.find_all('tr',class_='test',id='test')
trs=soup.find_all('tr',attrs={"id":"test","class":"test"})
# print(trs)

#获取a标签链接
# alist=soup.find_all('a')
# for a in alist:
#     #通过下标
#     href=a['href']
#     # print(href)
#     #通过属性
#     href = a.attrs['href']

#从列表第二个到最后个
trs=soup.find_all('tr')[1:-1]
movies=[]
for tr in trs:
    movie={}
#     tds=tr.find_all('td')
#     title=tds[0].string
#     categry=tds[1].string
#     movie['title']=title
#     movie['categry']=categry
#     movies.append(movie)
#
# print(movies)
    #strings获取所有的非标签的信息
    infos=list(tr.stripped_strings)
    movie['title']=infos[0]
    movie['categry']=infos[1]
    movies.append(movie)
print(movies)


#find_all和find区别：find_all是查找所有。find只查找一个
#获取属性有两个方法，一个是通过下标，一个是通过属性
#string只获得标签下的字符串
#strings返回子孙非标签字符串，返回生成器
#stripped_strings返回去掉空白的子孙非标签字符串，返回生成器
#get_text返回某个标签下子孙非标签字符串，不是列表形式返回，以普通字符串返回