# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubItem(scrapy.Item):
    movie_name=scrapy.Field()
    movie_data=scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
