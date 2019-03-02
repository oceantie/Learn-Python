from lxml import etree
import requests
BASE_DOMAIN='http://www.ygdy8.net'
url='http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html'
HEADERS={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',

}
def get_detail_urls(url):
    response = requests.get(url, headers=HEADERS)
#    text = response.content.decode('gbk')
    text = response.text
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url:BASE_DOMAIN+url,detail_urls)
    return detail_urls
def parse_detail_page(url):
    movie={}
    response=requests.get(url,headers=HEADERS)
    text=response.content.decode('gbk')
    html=etree.HTML(text)
    title=html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['title']=title

    zoomE=html.xpath('//div[@id="Zoom"]')[0]
    imgs=zoomE.xpath('.//img/@src')
    cover=imgs[0]
    screenshot=imgs[1]
    movie['cover'] = cover
    movie['screenshot'] = screenshot

    infos=zoomE.xpath('.//text()')

    def parse_info(info,rule):
        return info.replace(rule,'').strip()
    for index,info in enumerate(infos):
        # print(info)
        # print(index)

        #startswith以什么开始
        if info.startswith("◎年　　代"):
            info=parse_info(info,"◎年　　代")
            movie['year']=info
        elif info.startswith('◎产　　地'):
            info=parse_info(info,'◎产　　地')
            movie['country'] = info
        elif info.startswith('◎类　　别'):
            info=parse_info(info,'◎类　　别')
            movie['category'] = info
        elif info.startswith('◎豆瓣评分'):
            info = parse_info(info, '◎豆瓣评分')
            movie['douban_rating'] = info

        elif info.startswith('◎片　　长'):
            info = parse_info(info, '◎片　　长')
            movie['duration'] = info

        elif info.startswith('◎主　　演'):
            info = parse_info(info, '◎主　　演')
            actors=[info]
            for x in range(index+1,len(infos)):
                actor=infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            # print(actors)
            movie['actors'] = actors
    return movie


    # for x in title:
    #     print(etree.tostring(x,encoding='utf-8').decode('utf-8'))

def spider():
    base_url="http://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html"
    movies=[]
    #第一个for循环是用来控制7页的
    for x in range(1,8):
        url=base_url.format(x)
        detail_urls=get_detail_urls(url)
        #第二个for循环是用来遍历一页中所有电影详情页的地址
        for detail_url in detail_urls:
            movie=parse_detail_page(detail_url)
            movies.append(movie)
            #print(detail_url)
            print(movie)
        #     break
        # break
    # print(movies)
if __name__ == '__main__':
    spider()










