#!/usr/bin/python
# -*-coding:utf-8 -*-
def matches(text):
    print "输入请包含",text,'的字符串'
    while True:
        line=yield              #在使用send函数后把send的参数发送给yield并赋值给line
        if text in line:
            print line


def countdown(n):
    while n>0:
        yield n
        n -= 1

n=int(raw_input(' 请输入一个数字：'))
for i in countdown(n):
    print i
mat=matches(raw_input('请输入字符串（用于匹配确定）：'))
mat.next()
n=""
while n!='quit':
    n = raw_input('请输入一个字符串：')
    mat.send(n)
mat.close()