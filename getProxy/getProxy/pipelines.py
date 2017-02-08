# -*- coding: utf-8 -*-
import pymysql
import pymysql.cursors
from scrapy.exceptions import DropItem
from getProxy import items
import scrapy


class GetproxyPipeline(object):
  def __init__(self, dbparams):
    self.dbparams = dbparams

  @classmethod
  def from_crawler(cls, crawler):
    dbparams=dict(
            host=crawler.settings['MYSQL_HOST'],
            db=crawler.settings['MYSQL_DBNAME'],
            user=crawler.settings['MYSQL_USER'],
            passwd=crawler.settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
            )

    return cls(
        dbparams=dbparams,
        )

  #spider开启时，该方法被执行，连接数据库
  def open_spider(self, spider):
    self.connection = pymysql.connect(**self.dbparams)
    
  #spider关闭时，该方法被执行
  def close_spider(self, spider):
    self.connection.close()

  def process_item(self, item, spider):
    if hasattr(item, "saveto_mysql"):
      if callable(item.saveto_mysql):
        item.saveto_mysql(self.connection)
    return item

  
  def saveto_mysql(self,db):
    print('4'*446)
    ip = self.get('ip', 0)
    port = self.get('port', 0)
    proxyType = self.get('proxyType', 0)
    loction = self.get('loction', 0)
    upDated = self.get('upDated', 0)
    score = self.get('score', 0)
    allScore = self.get('allScore', 0)
    useTime = self.get('useTime', 0)
    speed = self.get('speed', 0)
    protocol = self.get('protocol',0)
    source = self.get('source',0)
    print(ip)

    try:
        with db.cursor() as cursor:
            sql = "INSERT INTO `myproxy` (ip, port,proxyType,loction,upDated,score,allScore,useTime,protocol,source) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s,%s)"
            data = (ip,port,proxyType,loction,upDated,score,allScore,useTime,protocol,source)
            cursor.execute(sql, data)
        db.commit()
    except Exception as e:
        print("save myproxy fail %s" % e)



    # CREATE TABLE myproxy (
    #  id int not null auto_increment,
    #  ip varchar(32) null,
    #  port varchar(32) null,
    #  proxyType varchar(32) null,
    #  loction varchar(32) null,
    #  upDated varchar(32) null,
    #  score varchar(32) null,
    #  allScore varchar(32) null,
    #  useTime varchar(32) null,
    #  protocol varchar(32) null,
    #  source varchar(32) null,
    #  primary key(id)
    #  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户信息表';