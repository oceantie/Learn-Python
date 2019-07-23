import requests
import pandas as pd
import time
import csv

key='c6f9f173e3b10c8032b1f9396d492e73'
#BASE_URL='https://restapi.amap.com/v3/place/text?keywords=%E6%98%9F%E5%B7%B4%E5%85%8B&city=028&output=json&offset=20&page={}&key=c6f9f173e3b10c8032b1f9396d492e73&extensions=all'
BASE_URL='https://restapi.amap.com/v3/place/text?keywords=%E6%98%9F%E5%B7%B4%E5%85%8B&city={}&output=json&offset=20&page={}&key=c6f9f173e3b10c8032b1f9396d492e73&extensions=all'
STARBUCKS_PROVINCE=[]
STARBUCKS_CITY=[]
STARBUCKS_NAME=[]
STARBUCKS_ADDRS=[]
def get_startbucks_data():
    csv_data = pd.read_csv('AMap_adcode_citycode2.csv')
    for index,row in csv_data.iterrows():
        page=1
        while 1:
            try:
                url=BASE_URL.format(row['adcode'],page)
                res=requests.get(url).json()
                startbucks=res.get('pois')
                print('正在爬取',row['中文名'],page,'页')
                if int(res['count'])>0:
                    for startbuck in startbucks:
                        province=startbuck['pname']
                        city=startbuck['cityname']
                        name=startbuck['name']
                        address=startbuck['address']
                        STARBUCKS_PROVINCE.append(province)
                        STARBUCKS_CITY.append(city)
                        STARBUCKS_NAME.append(name)
                        STARBUCKS_ADDRS.append(address)
                        #print(page)
                    page += 1
                else:
                     print('城市:{}第{}页无数据!'.format(row['中文名'], page))
                     break
                time.sleep(1)
            except:
                time.sleep(5)
                pass
    #    print(row['citycode'])
def write_csv():
    starbuckData = pd.DataFrame({'province': STARBUCKS_PROVINCE, 'city': STARBUCKS_CITY,'name':STARBUCKS_NAME,'address':STARBUCKS_ADDRS})
    print(starbuckData)
    starbuckData.to_csv("startbucks.csv", index=False, sep=',',encoding="utf_8_sig")#encoding="utf_8_sig"才能写入csv，否则为乱码
# def parse_data(url):
#     res=requests.get(url).json()
#     startbucks=res.get('pois')
#     if startbucks is not None:
#         for startbuck in startbucks:
#             name=startbuck['name']
#             address=startbuck['address']
#             print(name,address)
#             time.sleep(0.2)
#     else:
#         return
# def get_page():
#     for x in range(1,9):
#         print('正在爬取第',x,'页')
#         url=BASE_URL.format(x)
#         # print(url)
#         parse_data(url)

if __name__ == '__main__':
    get_startbucks_data()
    write_csv()

