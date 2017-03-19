from scrapy.spiders import Spider
from Fridge.items import FridgeCrawlItem
from scrapy.http import Request


class FridgeSpider(Spider):
	name = "Fridgy"
	allowed_domains = ["http://www.technomarket.bg"]
	start_urls = ["http://www.technomarket.bg/hladilnitzi"]

	def parse(self, response):
		for path in response.xpath('//figcaption'):
			item = FridgeCrawlItem()
			item["price"] = path.xpath('div[2]/var/span[1]/text()').extract()
			item["title"] = path.xpath('div[1]/h3/a/span/text()').extract()
			yield item
