#!/usr/bin/python

# -*- coding: UTF-8 -*- 

import MySQLdb

class WebCrawlerDB:

    db = MySQLdb.connect("localhost", 'root', "root", 'spider')
    cursor = db.cursor()
        
    @staticmethod
    def write(sql):
        if sql.strip():
            try:
                WebCrawlerDB.cursor.execute(sql)
                WebCrawlerDB.db.commit()
            except:
                print "db write error"
                WebCrawlerDB.db.rollback()
    @staticmethod
    def read(sql):
        if sql.strip():
            try:
                WebCrawlerDB.cursor.execute(sql)
                results = WebCrawlerDB.cursor.fetchall()
                return results 
            except:
                print "db operate Error:unable to fetch data"


if __name__ == '__main__':
     sql = "insert into test(id, name) values(2, 'zhihao');"   
     #WebCrawlerDB.write(sql)
     sql = "select * from test";
     results = WebCrawlerDB.read(sql)
# need conveert python sql to python class and auto assign value ,  generate a direct
# use python object
     for row in results:
         ID = row[0]
         name = row[1]
         print "ID:%d name:%s " % (ID, name)
