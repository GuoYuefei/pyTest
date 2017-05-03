#!/usr/bin/python
#!coding:utf8
#这个模块用来测试练习使用re模块来处理正则表达式
import re
s="qwertyuiopasdfhboyqweweaboydasboy"
res=re.findall("\w*boy[q]",s,re.I)
print res
print len(res)

#文件内容的查找
f1=file('./../../fileTest/111.py',"r",1)
count=0
for s in f1.readlines():
    li = re.findall("x",s)
    if len(li)>0:
        count+=len(li)
print "查找到"+str(count)+"个x"

#文件的复制包括替换
f1.seek(0,0)        #文件指针指向文件头
f2=file('./../../fileTest/222',"w",1)
for s in f1.readlines():
    f2.write(s.replace("x","a"))        #将x替换成a，replace函数是不支持正则表达式的
f1.close()
f2.close()