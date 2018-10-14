# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItItem(scrapy.Item):
   title = scrapy.Field()
   url = scrapy.Field()
   img_url = scrapy.Field()
   introduction = scrapy.Field()
   student = scrapy.Field()
   image_path = scrapy.Field()