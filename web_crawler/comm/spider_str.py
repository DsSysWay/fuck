
#!/usr/bin/python
# -*- coding: utf-8 -*-



class WebCrawlerStrTool:
    @staticmethod
    def  findAndCut(src,cutWord):
        if  src.strip() and  cutWord.strip():
            return src.replace(cutWord, "")

    @staticmethod
    def  delFirstAndLastChar(src):
        if  src.strip(): 
            length = len(src)
            if length >= 1:
                return  src[1:(length - 1)] 

    @staticmethod
    # position -1 means get the last one
    def splitAndFetchByPosition(src, splitWord, position): 
        if src.strip() and splitWord.strip():
            srcList = src.split(splitWord)
            length =  len(srcList)
            if length > 0 :
                if position < length:
                    return srcList[position]
                if  position == -1:
                    return srcList[length - 1]




