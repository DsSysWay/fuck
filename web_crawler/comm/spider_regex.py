#!/usr/bin/python
# -*- coding: utf-8 -*-




import re


class WebCrawlerRegexTool:

    @staticmethod
    def patternExtract(src,pattern):
        # src not null
        if  src.strip():
            rePattern = re.compile(pattern)
            matchGroup = rePattern.search(src)
            if matchGroup:
                 hrefStr =  matchGroup.group()
                 return hrefStr
            else:
                print "hrefStr is null"  





if __name__ == '__main__':
    hrefStr  = '<a href="/article/WorkLife/1568">我的华为3Com两年ZZ</a>'
    href = WebCrawlerRegexTool.patternExtract(hrefStr,"href=(.*)\"")
    print "href:" + str(href)
