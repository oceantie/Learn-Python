from lxml import etree
import requests

url='http://www.scxdfxx.com/plus/diy.php?action=list&diyid=1&totalresult=31&pageno=1'
proxies={
    'https':'14.20.235.203:9797',
    'http':'211.162.70.229:3128'

}
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
             'Connection': 'keep-alive'}
#html=requests.get(url,proxies)

# with open('info.html','w',encoding='utf-8') as f:
#      f.write(html.text)
parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('info.html',parser=parser)
name_list=[]
phone_list=[]
ip_list=[]
timr_list=[]
tables=html.xpath('/html/body/div[1]/div[2]/div[2]/div/table[@cellspacing="1"]')

# names=html.xpath('/html/body/div[1]/div[2]/div[2]/div/table/tbody/tr[2]/td[2]')
# phones=html.xpath('/html/body/div[1]/div[2]/div[2]/div/table/tbody/tr[3]/td[2]')
# for tr in names:
#     name_list.append(tr.text)
# for phone in phones:
#     phone_list.append(phone.text)
# print(phone_list)
print(len(tables))
for tab in tables:
    names = tab.xpath('.//tbody/tr[2]/td[2]')
    print(names[0].text)



