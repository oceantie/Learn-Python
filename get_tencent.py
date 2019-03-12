
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

url = "https://hr.tencent.com/position.php"
url2="https://hr.tencent.com/position.php?keywords=&tid=0&lid=2268"
BASED_URL='https://hr.tencent.com/'
pageNumber_url='https://hr.tencent.com/position.php?keywords=&tid=0&lid=2268&start={}#a'
jobs=[]

# urllist = []
#在列表页后去本页详情页的url
def get_page_urllist(url):
    urllist = []
    response = requests.get(url, headers=headers).text
    soup=BeautifulSoup(response,'lxml')
    joblist=soup.find_all('tr',class_=['even','odd'])
    #获取每个职位详情页的url
    for job in joblist:
        a=job.find_all('a')
        get_pageInfo(BASED_URL+a[0].attrs['href'])


#获取每个详情页的相关信息
def get_pageInfo(url):
    position = {}
    response=requests.get(url,headers=headers).text
    soup=BeautifulSoup(response,'lxml')
    title=soup.find_all('td',id='sharetitle')[0].get_text()
    position['title']=title
    require1=soup.find_all('ul',class_='squareli')[0].get_text()
    require2 = soup.find_all('ul', class_='squareli')[1].get_text()
    # print(require2)
    position['require1']=require1
    position['require2'] = require2
    # print(position)
    jobs.append(position)

for x in range(0,3):
    url=pageNumber_url.format(x*10)
    get_page_urllist(url)
print(jobs)
    # print(url)
    # print("="*20)



