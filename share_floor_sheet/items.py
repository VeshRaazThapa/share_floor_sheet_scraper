# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShareFloorSheetItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    transact_no = scrapy.Field()
    symbol = scrapy.Field()
    buyer = scrapy.Field()
    seller = scrapy.Field()
    quantity = scrapy.Field()
    rate = scrapy.Field()
    amount = scrapy.Field()

    # designation = scrapy.Field()
    # email = scrapy.Field()
    # url = scrapy.Field()
    # office = scrapy.Field()
