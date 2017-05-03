#!/usr/bin/python
# -*-coding:gbk-*-
import py_compile
fileName=raw_input("请输入需要编译的文件的相对目录名:\n")
py_compile.compile(fileName)