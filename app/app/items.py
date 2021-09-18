# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZennArticlesItem(scrapy.Item):
    url = scrapy.Field()
    article_type = scrapy.Field()
    title = scrapy.Field()
    likes = scrapy.Field()
    date = scrapy.Field()
