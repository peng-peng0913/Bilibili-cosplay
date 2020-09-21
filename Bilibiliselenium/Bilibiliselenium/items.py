# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliseleniumItem(scrapy.Item):
    id1 = scrapy.Field()
    title = scrapy.Field()
    image = scrapy.Field()
    url = scrapy.Field()
    view1 = scrapy.Field()
    like1 = scrapy.Field()
    reply = scrapy.Field()