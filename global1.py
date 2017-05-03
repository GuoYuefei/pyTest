#!/usr/bin/python
# -*-coding:utf-8-*-
class GlobalTest:
    _a = 3
    _b = 6
    def sum(self):
        return self._a+self._b

globalTest = GlobalTest()
print globalTest.sum()