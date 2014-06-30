from scrapy.item import Item, Field
class LivingSocialDeal(Item):
	"""Livingsocial container (dictionary-like object) for scraped data"""
	title = Field()
	decription = Field()
	link = Field()
	category = Field()
	locaton = Field()
	original_price = Field()
	price = Field()