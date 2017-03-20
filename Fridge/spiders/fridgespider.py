from scrapy.spiders import Spider
from Fridge.items import FridgeCrawlItem
from scrapy.http import Request


class FridgeSpider(Spider):
	name = "Fridgy"
	allowed_domains = ["http://www.technomarket.bg"]

	start_urls_generator = (("http://www.technomarket.bg/product/filter?filter_form[sort]=price&filter_form[price][min]=159"
							"&filter_form[price][max]=4599&filter_form[spec_volume_refrigerator][min]="
							"&filter_form[spec_volume_refrigerator][max]=&filter_form[spec_volume_freezer][min]="
							"&filter_form[spec_volume_freezer][max]="
							"&filter_key=%2Fhladilnitzi%7Cstatic%7Cstatic&from={}&size=20").format(items*20) for items in range(0,20))

	start_urls = list(start_urls_generator)

	def parse(self, response):
		for path in response.xpath('//figcaption'):
			item = FridgeCrawlItem()
			item["price"] = path.xpath('div/var/span/text()').extract()
			item["title"] = path.xpath('div/h3/a/span/text()').extract()
			yield item
