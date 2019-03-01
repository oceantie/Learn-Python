import requests
from lxml import etree
url='https://movie.douban.com/cinema/nowplaying/chengdu/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
}
response=requests.get(url,headers=headers)
text=response.text
movise=[]
html=etree.HTML(text)
#print(etree.tostring(html,encoding='utf-8').decode('utf-8'))
uls=html.xpath('//ul[@class="lists"]')[0]
lis=uls.xpath('./li')
for li in lis:
    name=li.xpath('@data-title')[0]
    score=li.xpath('@data-score')[0]
    duration = li.xpath('@data-duration')[0]
    movie={
        'name':name,
        'score':score,
        'duration':duration
    }
    movise.append(movie)

print(movise)