#!/usr/bin/python
#!coding:utf8
#文件读取的一些练习
f=file("/home/fly/PycharmProjects/fileTest/111.py",'r',1)
x=f.readline()
while x!='':
    print x,
    x=f.readline()
#f.close()
print '\n'
f.seek(0,0)         #将文件指针返回到文件的开头
y=f.readlines()
print y

print '\n','开始测试os模块及其子模块'
import os
import time
print os.path.abspath('.')                  #可以返回当前工作目录的绝对路径
print os.path.dirname("/home/fly/PycharmProjects/fileTest/111.py")  #返回该路径的目录
print os.path.exists("/home/fly/PycharmProjects/fileTest")   #判断文件是否存在 （在系统中文件夹是特殊的文件）
print
#返回文件最后一次访问的时间,这个时间是距离1970.1.1的长整形时间s
s=os.path.getatime("/home/fly/PycharmProjects/fileTest/111.py")
print s
t=time.ctime(s)             #调用ctime可以把长整形的时间转换成正常的时间
#print time.strftime("%Y-%m-%d %H:%M:%S",t)     只有localtime这种结构体时间的才能使用这个函数
print t
print time.localtime()

print os.stat("/home/fly/PycharmProjects/fileTest/111.py")          #文件的所有属性






