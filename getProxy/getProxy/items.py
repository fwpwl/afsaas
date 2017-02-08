# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import pymysql

class GetproxyItem(scrapy.Item):

	ip = scrapy.Field()
	port = scrapy.Field()
	proxyType = scrapy.Field()
	loction = scrapy.Field()
	upDated = scrapy.Field()
	score = scrapy.Field()
	allScore = scrapy.Field()
	useTime = scrapy.Field()
	protocol = scrapy.Field()
	source = scrapy.Field()

	# def saveto_mysql(self,db):

	# 	ip = self.get('ip', 0)
	# 	port = self.get('port', 0)
	# 	proxyType = self.get('proxyType', 0)
	# 	loction = self.get('loction', 0)
	# 	upDated = self.get('upDated', 0)
	# 	score = self.get('score', 0)
	# 	allScore = self.get('allScore', 0)
	# 	useTime = self.get('useTime', 0)
	# 	speed = self.get('speed', 0)
	# 	protocol = self.get('protocol',0)
	# 	source = self.get('source',0)

	# 	try:
	# 		with db.cursor() as cursor:
	# 			sql = "INSERT INTO `myproxy` (ip, port,proxyType,loction,upDated,score,allScore,useTime,protocol,source) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s,%s)"
	# 			data = (ip,port,proxyType,loction,upDated,score,allScore,useTime,protocol,source)
	# 			cursor.execute(sql, data)
	# 		db.commit()
	# 	except Exception as e:
	# 		print("save myproxy fail %s" % e)
