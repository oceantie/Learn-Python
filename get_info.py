from lxml import etree
import requests
import xlsxwriter

base_url = "http://www.scxdfxx.com/plus/diy.php?action=list&diyid=1&totalresult=31&pageno={}"
#base_url="http://www.scxdf.com/plus/diy.php?action=list&diyid=18&totalresult=59&pageno={}"
proxies={
    'https':'14.20.235.203:9797',
    'http':'211.162.70.229:3128'

}
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
             'Connection': 'keep-alive'}
#
form_info = []
def get_detail(url):

    response = requests.get(url,proxies)
    text=response.text
    html=etree.HTML(text)
    tables = html.xpath('/html/body/div[1]/div[2]/div[2]/div/table[@cellspacing="1"]')
    for tab in tables:
        names = tab.xpath('.//tbody/tr[2]/td[2]/text()')
        phone = tab.xpath('.//tbody/tr[3]/td[2]/text()')
        time=tab.xpath('.//tbody/tr[4]/td[2]/text()')
        url = tab.xpath('.//tbody/tr[5]/td[2]/text()')
        info={
            'name':names,
            'phone': phone,
            'time':time,
            'url':url,
        }
        form_info.append(info)

def write_excel(file_neme,form_info):
    workbook = xlsxwriter.Workbook(file_neme) # 建立文件
    worksheet = workbook.add_worksheet('') # 建立sheet， 可以work.add_worksheet('employee')来指定sheet名，但中文名会报UnicodeDecodeErro的错误
    for index,li in enumerate(form_info):
        print(form_info[index]['name'])
        print(form_info[index]['time'])
        print(form_info[index]['url'])
        print(form_info[index]['phone'])
        worksheet.write(index, 0, form_info[index]['name'][0])  # 向第一列写入name
        worksheet.write(index, 1, form_info[index]['phone'][0])  # 向第一列写入phone
        worksheet.write(index, 2, form_info[index]['time'][0])  # 向第二列写入time
        worksheet.write(index, 3, form_info[index]['url'][0])  # 向第三列写入url
    workbook.close()

#对每页遍历
def spider(num):
    for x in range(1,num+1):
        url = base_url.format(x)
        get_detail(url)
    write_excel('xdf_info3.xlsx',form_info)

spider(5)