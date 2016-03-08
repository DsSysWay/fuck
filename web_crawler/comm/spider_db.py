#coding=utf-8
#!/usr/bin/python


import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class WebCrawlerDB:

    db = MySQLdb.connect("localhost", 'root', "root", 'spider', charset="utf8" )
    cursor = db.cursor()
    cursor.execute('SET NAMES utf8')
        
    @staticmethod
    def write(sql):
        if sql.strip():
            try:
                WebCrawlerDB.cursor.execute(sql)
                WebCrawlerDB.db.commit()
            except MySQLdb.Error,  e:
                WebCrawlerDB.db.rollback()
                try:
                   print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
                except:
                   print 'mysql write error'
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
     sql = "insert into attritube(title, url, source) values('志豪','志豪', '志豪')"
     print "sql:%s" % sql
     WebCrawlerDB.write(sql)
     sql = "select *  from attritube order by id desc limit 2";
     results = WebCrawlerDB.read(sql)
# need conveert python sql to python class and auto assign value ,  generate a direct
# use python object
     for row in results:
         title = row[1].decode("utf-8")
         print "title:%s " % (title)
