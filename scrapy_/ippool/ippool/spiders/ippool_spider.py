# -*- coding: utf-8 -*-
import scrapy
import json

class IppoolSpiderSpider(scrapy.Spider):
    name = 'ippool_spider'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        origin = json.loads(response.text)['origin']
        print("="*30)
        print('the sever returm:'+origin)
        print("=" * 30)
        yield scrapy.Request(self.start_urls[0], dont_filter=True)
