import scrapy

from price.items import Product

class Flipkart(scrapy.Spider):
	name = "flipkartSpider"
	allowed_domains = ["flipkart.com"]
	start_urls = [
	"http://www.flipkart.com/laptops/pr?sid=6bo,b5g#/jumpTo=371%7C998"
	]

	def parse(self, response):
		for a in response.xpath('//div[@class="pu-title fk-font-13"]/a/text()').extract():
			yield Product(name=a)
		for amount in response.xpath('//div[@class="pu-final"]/span/text()').extract():
			yield Product(price=amount)

'''
	def parse_torrent(self, response):
		prod = Product()
		prod['name'] = response.xpath('//div[@class="pu-title fk-font-13"]/a/text()').extract()
		prod['pprice'] = response.xpath('//div[@class="pu-final"]/span/text()').extract()
		return prod
'''