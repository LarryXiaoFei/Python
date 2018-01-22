
"""
@desc:类的使用
@date:2018-01-22
@author:Walter
"""
class Employee:
    #公有变量定义
    empCount=0
    #私有变量定义
    __age=20

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1

    def displayCount(self):
        print("Total Count is %d" % Employee.empCount)

    def dispalyEmployee(self):
        print("NAME is",self.name,"Salary IS",self.salary)

    #定义私有变量调用接口函数
    def displayAge(self):
        print("年龄是%d" % Employee.__age)
