import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
import pymysql
import time

user_agent = 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 wechatdevtools/0.7.0 MicroMessenger/6.3.9 Language/zh_CN webview/0'
target_url='https://m.weibo.cn/api/statuses/repostTimeline?id=4362729449834537&page={}'
id_url='https://m.weibo.cn/api/container/getIndex?type=uid&value={}'
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/1665372775',
    'User-Agent': user_agent
}

def get_user_id(url):  #获取该微博下转发者的id号
    response = requests.get(url,headers)
    json = response.json()
    datas = json.get('data').get('data')
    for data in datas:
        id=data.get('user').get('id')
        print(id)
        parse_pageById(id)  #获取到id之后，再对每个id进行解析
user_list=[]
def parse_pageById(id):
    url=id_url.format(id)
    # print(url)
    response = requests.get(url, headers) #个人信息的url需要url和id拼接
    json = response.json()
    try:
        user_name=json.get('data').get('userInfo').get('screen_name')
        followers_count=json.get('data').get('userInfo').get('followers_count')
        follow_count = json.get('data').get('userInfo').get('follow_count')
        weibo_count = json.get('data').get('userInfo').get("statuses_count")
        sex = json.get('data').get('userInfo').get("gender")
        user_data={
            'user_name':user_name,
            'followers_count':followers_count,
            'follow_count':follow_count,
            'weibo_count':weibo_count,
            'sex':sex,
        }
        print(user_data)
        user_list.append(user_data)
    except:
        user_data = {
            'user_name': 'balnk',
            'followers_count': 'balnk',
            'follow_count': 'balnk',
            'weibo_count': 'balnk',
            'sex': 'balnk',
        }
        user_list.append(user_data)
    # print(user_list)
def get_singleUserUrl(base_url):#对单个用户的页面数据进行解析
    for x in range(20,40):  #
        print('页数:',x)
        url=base_url.format(x)
        get_user_id(url)
        time.sleep(2)
        # print(url)

# 写入数据库
def write_in_Mysql():
    print(user_list)
    for x in user_list:#遍历用户列表
        print(x)
        conn=pymysql.connect(host='localhost',user='root',password='123456',database='weibo',port=3306)#开启自己的数据库
        cursor=conn.cursor()
        sql="""
        insert into weibo_data(id,user_name,followers_count,follow_count,weibo_count,sex) values (null,%s,%s,%s,%s,%s)
        """
        cursor.execute(sql,(x['user_name'],x['followers_count'],x['follow_count'],x['weibo_count'],x['sex']))
        conn.commit()
        cursor.close()

def run():
    get_singleUserUrl(target_url)
    write_in_Mysql()

if __name__ == '__main__':
    run()
