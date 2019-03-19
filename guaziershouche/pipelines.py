# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GuaziershouchePipeline(object):
    def process_item(self, item, spider):
        return item

from scrapy.exceptions import DropItem
class DuplicatesPipeline(object):
    def __init__(self):
        self.data = set()

    def process_item(self, item, spider):
        if item['car_url'] in self.data:
            raise DropItem("Duplicate item found")
        else:
            self.data.add(item['car_url'])
            return item


from scrapy.conf import settings
from twisted.enterprise import adbapi
import pymysql
from pymysql import cursors

class MysqlTwistedPipeline(object):
    def __init__(self):
        dbparms={
            'host': settings['MYSQL_HOST'],
            'port': settings['MYSQL_PORT'],
            'user' :settings['MYSQL_USER'],
            'password' : settings['MYSQL_PASSWORD'],
            'database' : settings['MYSQL_DBNAME'],
            'charset' : 'utf8',
            'cursorclass':cursors.DictCursor
        }
        self.dbpool=adbapi.ConnectionPool('pymysql',**dbparms)

    def process_item(self,item,spider):
        query=self.dbpool.runInteraction(self.do_insert,item)
        query.addErrback(self.handle_error,spider)

    def handle_error(self,failure,spider):
        print(failure)

    def do_insert(self,cursor,item):
        item_data = (item['car_brand'], item['car_url'], item['mile'], item['buy_year'], item['sale_price'], item['original_price'])
        sql = "insert into ershouche(car_brand,car_url,mile,buy_year,sale_price,original_price)VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,item_data)

import pymongo
class MongDBPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbName = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        tdb = client[dbName]
        self.post = tdb[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        bookInfo = dict(item)
        self.post.insert(bookInfo)
        return item