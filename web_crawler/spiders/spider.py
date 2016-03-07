#coding="utf-8"
import  re
import json


from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle


from web_crawler.items import *
from web_crawler.misc.log import *
from web_crawler.comm.spider_str import  *
from web_crawler.comm.spider_regex import  *
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


###URL2_ARTICLE_TITLE = {}

#z_c0 _xsrf is key cookie 
class web_crawlerSpider(CrawlSpider):

    MAX_PARSE_PEOPLE_NUM = 100

    BASE = "https://bbs.byr.com"

    headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, sdch",
            "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
            "Cookie":"login-user=zhihao; nforum[UTMPUSERID]=zhihao; nforum[PASSWORD]=gkNh0un%2BmiBDwPpINtY29g%3D%3D; nforum[UTMPKEY]=9655420; nforum[UTMPNUM]=3726; nforum[XWJOKE]=hoho; nforum[BMODE]=2; Hm_lvt_38b0e830a659ea9a05888b924f641842=1456745963,1456923415,1456984507,1457096883; Hm_lpvt_38b0e830a659ea9a05888b924f641842=1468108437; left-index=0001000000",
            "DNT":"1",
            "Host":"bbs.byr.cn",
            "Referer":"http://bbs.byr.cn/",
            "If-Modified-Since":"Fri, 04 Mar 2016 15:20:41 GMT",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36",
            "X-Requested-With":"XMLHttpRequest",
            }

    cookies = {
            }



    name = "web_crawler" #here is the key to name spider,if not match will throw spider not found error
    allowed_domains = ["bbs.byr.com"]
    start_urls = [
            "http://bbs.byr.cn/board/WorkLife?_uid=zhihao&p=118"
            #program zhuan lan
    ]
    rules = [
      #  Rule(sle(allow=("/followees")), follow=True, callback='parse_follow'),
      #  Rule(sle(allow=("/collections")), follow=True, callback='parse_collection'),
    ]



    def __init__(self):
        info('init start')
        return

    def start_requests(self): 
        info("start url:"+ self.start_urls[0])
        yield  scrapy.Request(url=self.start_urls[0],callback=self.parse_essence, headers=self.headers,cookies=self.cookies);
        #yield  scrapy.Request(url=self.start_urls[0],callback=self.parse_collection_list, headers=self.headers,cookies=self.cookies);

    baseUrl = "http://bbs.byr.cn/#!"
    def parse_essence(self, response):
        trSelector = response.xpath("//tbody/tr")
        for selector in trSelector:
            isMarkSelector = selector.xpath('./td[contains(@class,"title_8")]/a/samp/@class')
            isMarkStr = isMarkSelector.extract()[0]
            isMark = isMarkStr.endswith("-m")
            info("isMark:" + str(isMark))
            
            tieziSelector = selector.xpath("./td[contains(@class,'title_9')]/a[contains(@href,'/article')]").extract() 
            titleStr =  WebCrawlerRegexTool.patternExtract(tieziSelector[0],">(.*)<")
            title = WebCrawlerStrTool.delFirstAndLastChar(titleStr)
            if title.startswith("Re"):
                info("tiezi has been del")
                continue
            hrefStr =  WebCrawlerRegexTool.patternExtract(tieziSelector[0],"href=(.*)\"")
            urlStr = WebCrawlerStrTool.findAndCut(hrefStr,"href=")
            url = WebCrawlerStrTool.delFirstAndLastChar(urlStr)
            ID = WebCrawlerStrTool.splitAndFetchByPosition(url, "/", -1) 
            url = self.baseUrl + url
            info("url:" + url)
            info("ID:" + ID)
            info("title:"+title)
            timeSelector = selector.xpath("./td[@class='title_10']/text()").extract() 
            info("time:"+ str(timeSelector))

        



    def _process_request(self, request):
        info('process ' + str(request))
        return request

