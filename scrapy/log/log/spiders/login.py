import scrapy

from scrapy.http import Request

class LoginSpider(scrapy.Spider):
	name = 'keep'
	start_urls = ['https://www.flipkart.com/affiliate/login']
	
	def parse(self, response):
		return scrapy.FormRequest.from_response(
		response,
		formdata={'email': 'vaibhavmule135@gmail.com', 'password': '9860819262'},
		callback=self.after_login
		)
		'''
	def logged_in(self, response):
		# here you would extract links to follow and return Requests for
		# each of them, with another callback
		pass
		'''

	def after_login(self, response):
		# check login succeed before going on
		if "authentication failed" in response.body:
			self.log("Login failed", level=log.ERROR)
			return
		else:
			return Request(url="http://www.flipkart.com/landing",
               callback=self.parse)
			print response.xpath('//h1/text()').extract()
			