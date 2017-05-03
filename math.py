#!/usr/bin/python
# -*-coding:utf-8-*-
import math
x=3
y=4
print '%2.2f' % math.pi
x=raw_input("请输入你的分数：")
if x>='90':
    print "A"
elif '90'>x>='80':
    print "B"
elif '80'>x>='60':
    print "C"
else:
    print "D"