from scrapy.item import Item, Field
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import TakeFirst, MapCompose, Join,Compose

class FlipkartItem(Item):
    # define the fields for your item here like:
    # name = Field()
    productName=Field()