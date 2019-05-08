# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jiansu_spider.items import ArticleItem
import json

class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[a-z0-9]{12}.*'), callback='parse_detail', follow=True),
    )
    def parse_detail(self, response):
        title=response.xpath("//h1[@class='title']/text()").get()
        avator=response.xpath('//a[@class="avatar"]/img/@src').get()
        author=response.xpath('//span[@class="name"]/a/text()').get()
        pub_time=response.xpath('//span[@class="publish-time"]/text()').get().replace("*","")
        # print(pub_time)
        url=response.url
        # ['https://www.jianshu.com/p/f6f0ccfc5a5a','https://www.jianshu.com/p/0f2c5ccb79c4?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation']
        url1=url.split("?")[0]
        article_id=url1.split("/")[-1]
        content=response.xpath("//div[@class='show-content']").get()

        json_str = response.xpath("//script[@type='application/json']/text()").get()
        article_data = json.loads(json_str)
        word_count = article_data['note']['public_wordage']
        read_count = article_data['note']['views_count']
        comment_count = article_data['note']['comments_count']
        like_count = article_data['note']['likes_count']
        print(word_count)d

        # word_count=response.xpath('//span[@class="wordage"]/text()').get()
        # comment_count=response.xpath("//span[@class='comments-count']/text()").get()
        # like_count = response.xpath("//span[@class='likes-count']/text()").get()
        # read_count = response.xpath("//span[@class='views-count']/text()").get()
        subjects=",".join(response.xpath("//div[@class='include-collection']/a/div/text()").getall())

        item=ArticleItem(
            title=title,
            avator=avator,
            author=author,
            pub_time=pub_time,
            origin_url=response.url,
            article_id=article_id,
            content=content,
            comment_count=comment_count,
            subjects=subjects,
            word_count=word_count,
            like_count=like_count,
            read_count=read_count,

        )
        print(item)
        yield item

