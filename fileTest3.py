#!/usr/bin/python
#!coding:utf8

import os

#使用递归方式列出了一个文件夹下面的所有文件（包括子文件下的文件）
def visitDir(path):
    li = os.listdir(path)
    for p in li:
        pathname = os.path.join(path, p)
        if not os.path.isfile(pathname):
            visitDir(pathname)
        else:
            print pathname


if __name__ == "__main__":
    path = r"/home/fly/PycharmProjects"             #前面加r代表不转义
visitDir(path)
