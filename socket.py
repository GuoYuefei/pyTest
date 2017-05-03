#! /usr/bin/python
# -*-coding:utf-8-*-



import socket , sys

port = 80
host = 'www.baidu.com'
filename = raw_input("请输入访问的文件")

s=socket.socket(socket.AF_INET,socket.SOKE_STREAM)
try:
    s.connect((host,port))
except socket.gaierror,e:
    print "Error connecting to server:%s" % e
    sys.exit(1)
s.sendall(filename+"\r\n")
while 1:
    buf= s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)