# -*- coding: utf-8 -*-
import scrapy
from doub.items import DoubItem


class DoubSpiderSpider(scrapy.Spider):
    name = 'doub_spider'
    # // *[ @ id = "nowplaying"] / div[2] / ul
    allowed_domains = ['https://movie.douban.com/cinema/nowplaying/chengdu/']
    start_urls = ['https://movie.douban.com/cinema/nowplaying/chengdu//']

    def parse(self, response):
        doubans=response.xpath('//div[@id="nowplaying"]/div[2]/ul/li')
        for douban in doubans:
            movie_name=douban.xpath('@data-title')[0].get()
            movie_data=douban.xpath('@data-score')[0].get()
            item=DoubItem(movie_name=movie_name,movie_data=movie_data)
            yield item