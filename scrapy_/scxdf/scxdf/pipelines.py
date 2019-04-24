# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter
from openpyxl import Workbook

class ScxdfPipeline(object):
    def __init__(self):
        # self.fp=open('scxdf1.json','wb')
        # self.exporter=JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
        #
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['article_detail', 'title'])


    def process_item(self, item, spider):
        line = [item['article_detail'], item['title']]  # 把数据中每一项整理出来
        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        self.wb.save('file.xlsx')  # 保存xlsx文件
        # print(item)
        # self.exporter.export_item(item)
        return item
    def close_spider(self,spider):
        print('cloase')
        self.fp.close()


