# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # name = scrapy.Field()
    link = scrapy.Field()
    pass


class BookItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    pass
