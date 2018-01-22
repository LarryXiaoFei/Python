"""
@desc:引入所需模块
@date:2018-01-22
@author:Walter
"""
from trunk.class_test.employee import Employee





"""
入口函数
"""
if __name__=="__main__":
    print("开始")
    employ = Employee("张三",2000)
    # employ.dispalyEmployee()
    print("%d" % employ.empCount)
    employ.displayAge()


