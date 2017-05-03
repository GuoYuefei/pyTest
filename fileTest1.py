#!/usr/bin/python
#!coding:utf8
# 这个模块主要用于测试练习文件的操作
# 在linux下，换行只要\n，在windows下换行\r\n
f = file("/home/fly/PycharmProjects/fileTest/111.py",'w+',1)
print f.name
string1='#!/usr/bin/python\n'
string2='#!coding:utf8\n'
string3='def fun(x,y=0):\n'
string4='\tif(x==y):\n'
string5='\t\tprint "两个参数相等"\n'
string6='\telse:\n'
string7='\t\tprint "两个参数不相等"\n'
string8='fun(0)'
x=(string1,string2,string3,string4,string5,string6,string7,string8)
for i in xrange(len(x)):
    f.write(x[i])
#    f.flush()


