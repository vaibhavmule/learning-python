from scrapy.spider import Spider
from scrapy.selector import Selector
from flip.items import FlipkartItem

class Test(Spider):
    name = "flipkart"
    allowed_domains = ["flipkart.com"]
    start_urls = ["http://www.flipkart.com/moto-e/p/itmdvuwsybgnbtha"]

def parse_torrent(self, response):
        torrent = FlipkartItem()
        torrent['productName'] = response.xpath("//h1/text()").extract()
        return torrent