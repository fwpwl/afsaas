# -*- coding: utf-8 -*-
import scrapy
from getProxy.items import GetproxyItem

class Proxy360spiderSpider(scrapy.Spider):
	name = "proxy360Spider"
	allowed_domains = ["proxy360.cn"]
	nations = ['Brazil','China','America','Taiwan','Japan','Thailand','Vietnam','bahrein']
	start_urls = []
	for nation in nations:
		start_urls.append('http://www.proxy360.cn/Region/'+nation)


	def parse(self, response):
		subSelector = response.xpath('//div[@class="proxylistitem"and @ name="list_proxy_ip"]')
		items = []
		for sub in subSelector:
			item = GetproxyItem()
			item['ip'] = sub.xpath('.//span[1]/text()').extract()[0].strip()
			item['port'] = sub.xpath('.//span[2]/text()').extract()[0].strip()
			item['proxyType'] = sub.xpath('.//span[3]/text()').extract()[0].strip()
			item['loction'] = sub.xpath('.//span[4]/text()').extract()[0].strip()
			item['upDated'] = sub.xpath('.//span[5]/text()').extract()[0].strip()
			item['score'] = sub.xpath('.//span[6]/text()').extract()[0].strip()
			item['allScore'] = sub.xpath('.//span[6]/text()').extract()[0].strip()
			item['useTime'] = sub.xpath('.//span[7]/text()').extract()[0].strip()
			item['protocol']='HTTP'
			item['source'] = 'proxy360.cn'
			items.append(item)
		# yield item	
		return items
