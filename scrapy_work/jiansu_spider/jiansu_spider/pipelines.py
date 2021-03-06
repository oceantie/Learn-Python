# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors
#同步
class JiansuSpiderPipeline(object):
    def __init__(self):
        # dbparams={
        #     'host':'localhost',
        #     'port':'3306',
        #     'user':'root',
        #     'password': '123456',
        #     'database':'jianshu2',
        #     'charset':'utf8'
        # }
        # self.conn = pymysql.connect(host='localhost', user='root', password='123456', database='demo_python', port=3306)
        self.conn = pymysql.connect(host='localhost', user='root', password='123456', database='jianshu2', port=3306)
        # self.conn=pymysql.connect(**dbparams)
        self.cursor=self.conn.cursor()
        self._sql=None
        print("*" * 30)
    def process_item(self, item, spider):
        self.cursor.execute(self.sql,(item['title'],item['content'],item['author'],item['avator'],item['pub_time'],item['origin_url'],item['article_id']))
        self.conn.commit()
        return item
    @property
    def sql(self):
        if not self._sql:
            self._sql= """
            insert into article(id,title,content,author,avator,pub_time,origin_url,article_id) values (null,%s,%s,%s,%s,%s,%s,%s)
        """
            return self._sql
        return self._sql
#异步
class JiansuTwistedPipeline(object):
    def __init__(self):
        dbparams={
            'host':'localhost',
            'port':'3306',
            'user':'root',
            'password': '123456',
            'database':'jianshu2',
            'cursorclass':cursors.DictCursor
        }
        self.dbpool=adbapi.ConnectionPool('pymysql',host='localhost', user='root', password='123456', database='jianshu2', port=3306)
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
               insert into article(id,title,content,author,avator,pub_time,origin_url,article_id,read_count,like_count,word_count,comment_count,subjects) values (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
           """
            return self._sql
        return self._sql
    def process_item(self,item,spider):
        defer=self.dbpool.runInteraction(self.insert_item,item)
        defer.addErrback(self.handle_error,item,spider)

    def insert_item(self,cursor,item):
        cursor.execute(self.sql,(item['title'],item['content'],item['author'],item['avator'],item['pub_time'],item['origin_url'],item['article_id'],item['read_count'],item['like_count'],item['word_count'],item['comment_count'],item['subjects']))
    def handle_error(self,error,item,spider):
        print("="*10+'error'+"="*10)
        print('error')
        print("=" * 10 + 'error' + "=" * 10)
