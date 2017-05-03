#!/usr/bin/python
#!coding:utf8
import os,sys
import MySQLdb
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='test',charset="utf8")    #数据库连接,注意字符集的选择
except Exception,e:
    print e
    sys.exit()
cursor=conn.cursor()            #返回游标对象
sql = 'select *from users'
cursor.execute(sql)             #执行该条sql语句
data = cursor.fetchall()       #查询数据
if data:
    for x in data:
        for i in x:
            print i,"\t",
        print
cursor.close()
conn.close()