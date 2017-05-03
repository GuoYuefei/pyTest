#!/usr/bin/python
#! coding:utf8
#这个函数是不定参数的一个使用例子
def aaa(* args):
     print args
     for i in xrange(len(args)):
             print args[i]
     print args[1:len(args):2]

aaa(1,2,3,4,(1,2,3,4),'hello')

def fun(x,y=0):
    if(x==y):
        print '两个参数值相等'
fun(0)

