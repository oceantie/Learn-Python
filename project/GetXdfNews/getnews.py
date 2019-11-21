import requests
from lxml import etree
import openpyxl
import time
import csv
url_list=[]
xdf_data=[]
based_url='http://www.scxdf.com/news/hyxw/index_{}.html'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
}
# 获取列表页url
def get_listurl():
    for x in range(100):
        page_url=based_url.format(x)
        get_detailurl(page_url)
        print(x,"页")
# 获取每个列表页中的详情页url
def get_detailurl(url):
    response = requests.get(url, headers=headers)
    text=response.content
    html=etree.HTML(text)
    divs=html.xpath('//div[@class="news_lists clearf"]')
    for div in divs:
        url=div.xpath('./ul/li/a/@href')
        print(url[0])
        parse(url[0])
# 获取详情页数据
def parse(url):
    response=requests.get(url,headers=headers)
    try:
        text=response.content
        html=etree.HTML(text)
        # print(etree.tostring(html,encoding='utf-8').decode('utf-8'))
        title=html.xpath('//h1/text()')
        content_label = html.xpath('//div[@class="newsbd"]')[0]
        contents = content_label.xpath('string(.)')
        url=url
        data_all={
            'tilel':title,
            'url':url,
            'contents':contents
        }
        # xdf_data.append(data_all)
        write_csv(data_all)
        # print(xdf_data)
        time.sleep(1)
        print(data_all)
    except:
        pass
#数据存入csv
def write_csv(xdf_data):
   heade=['tilel','url','contents']
   with open('test2.csv', 'a', newline='',encoding='utf-8')as f:
       writer = csv.DictWriter(f, heade)
       writer.writerow(xdf_data)
       print("=================")

if __name__ == '__main__':
    get_listurl()
