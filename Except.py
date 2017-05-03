#!/usr/bin/python
#!coding:utf8
try:
    result = 10/0
except ZeroDivisionError:
    print "0不能作为除数"
except:
    print "程序异常"