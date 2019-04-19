# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scxdf.items import ScxdfItem

class ScxdfSpiderSpider(CrawlSpider):
    name = 'scxdf_spider'
    allowed_domains = ['scxdf.com']
    start_urls = ['http://www.scxdf.com/news/hyxw/index_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'.+index_\d+\.html'), follow=True),
        Rule(LinkExtractor(allow=r".+\d+\.html"), callback="parse_detail", follow=False)
    )

    def parse_detail(self, response):
        title=response.xpath("//div[@class='newshd']/h1/text()").get()
        article_detail=response.xpath("//div[@class='newshd']/p/text()").get()
        # print(article_detail)
        item=ScxdfItem(title=title,article_detail=article_detail)
        yield item
        # print(item)
