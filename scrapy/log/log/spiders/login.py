import scrapy

from scrapy.http import Request

class LoginSpider(scrapy.Spider):
	name = 'keep'
	start_urls = ['https://www.pinterest.com/login/']
	
	def parse(self, response):
		return scrapy.FormRequest.from_response(
		response,
		formdata={'username_or_email': 'vaibhavmule135@gmail.com', 'password': 'raj-13579'},
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
			print response.xpath('//span/text()').extract()
			