from lxml import etree
import requests
from urllib import request
import os
import re

Header={
     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53',
}
def get_pages(url):
   response=requests.get(url,headers=Header)
   text=response.text
   html=etree.HTML(text)
   # print(etree.tostring(html, encoding='utf-8').decode('utf-8'))
   images=html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
   # print(images[0].text)
   for img in images:
       img_url=img.get('data-original')
       alt=img.get('alt')
       #过滤图片标题后面的特殊符号
       alt=re.sub(r'[\?？\.，。！!…]',"",alt)
       suffix=os.path.splitext(img_url)[1]
       filname=alt+suffix
       request.urlretrieve(img_url,'images/'+filname)
       print(img_url)

def run():
    for x in range(5):
        url='https://www.doutula.com/photo/list/?page={}'
        # print(url.format(x))
        get_pages(url.format(x))
        break

if __name__ == '__main__':
    run()