# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MyanmarItem(scrapy.Item):
    name = scrapy.Field()
    cause_areas = scrapy.Field()
    location = scrapy.Field()
    website = scrapy.Field()
    programme_type = scrapy.Field()
    other_info = scrapy.Field()
    headcount = scrapy.Field()
    financials = scrapy.Field()
    established = scrapy.Field()
    religious = scrapy.Field()
    registered = scrapy.Field()
    outputs = scrapy.Field()
    mission = scrapy.Field()
    theory_of_change = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
