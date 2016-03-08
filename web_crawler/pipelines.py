# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html





import sys
import os
from scrapy import signals
from misc.log import *
from comm.spider_db import *
from items import *
import json
import codecs
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class webCrawlerPipeline(object):
    def process_item(self, item, spider):
        #info("item to db:"+ item['title'])
        #self.result.write(content)
        #self.result.flush()
        sql = "insert into attritube(title, url, posttime, mark, source, data ) values ('%s', '%s' , '%s', '%s', '%s', '%s' )" % (item['title'], item['url'], item["posttime"], item['mark'], item['source'], item['data'])
        info("sql:" + sql)
        WebCrawlerDB.write(sql)
        return item

if __name__ == '__main__':
    item = ByrTiezi()
    spider = 0
    item['url'] = "test"
    item['title'] = "test"
    item['posttime'] = "test"
    item['mark'] = "test"
    item['source'] = "test"
    pipe = webCrawlerPipeline()
    pipe.process_item(item, spider)
