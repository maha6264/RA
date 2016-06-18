# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class RaItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    start_url = Field()
    title = Field()
    category = Field()
    manufaturer = Field()
    image_url = Field()
    mfr_part = Field()
    sku = Field()
    upc = Field()
    upc14 = Field()

