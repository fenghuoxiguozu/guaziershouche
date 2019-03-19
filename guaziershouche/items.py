# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziershoucheItem(scrapy.Item):
    # define the fields for your item here like:
    car_brand = scrapy.Field()
    car_url = scrapy.Field()
    mile = scrapy.Field()
    buy_year = scrapy.Field()
    sale_price = scrapy.Field()
    original_price = scrapy.Field()



