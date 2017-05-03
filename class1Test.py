#!usr/bin/python
#!coding:utf8

__metaclass__ = type        #确定使用新式类
class Person:
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print "I'm %s" % self.name

person = Person()
person.setName("123")
print person.getName()
person.greet()