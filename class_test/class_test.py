"""
@desc:引入所需模块
@date:2018-01-22
@author:Walter
"""
from trunk.class_test.employee import Employee
import json



"""
@desc:dict转成obj
@date:2018-01-22
@author:Walter
"""
def obj_dic(d):
    top = type('new', (object,), d)
    seqs = tuple, list, set, frozenset
    for i, j in d.items():
        if isinstance(j, dict):
            setattr(top, i, obj_dic(j))
        elif isinstance(j, seqs):
            setattr(top, i,
                    type(j)(obj_dic(sj) if isinstance(sj, dict) else sj for sj in j))
        else:
            setattr(top, i, j)
    return top


"""
@desc:对象转字典
@date:2018-01-22
@author:Walter
"""
def props(obj):
    pr = {}
    for name in dir(obj):
        value = getattr(obj, name)
        if not name.startswith('__') and not callable(value):
            pr[name] = value
    return pr


"""
入口函数
"""
if __name__=="__main__":
    print("开始")
    # b={'a': 1, 'b': {'c': 2}, 'd': ['hi', {'foo': 'bar'}]}
    # x = obj_dic(b)
    # print(x.a,x.b.c)
    # y=x.d
    # t = y[1]
    # print(t.foo)



    # employ = json.loads('{"name":"rumor","salary":25}',Employee.__class__)
    employ = Employee("张三",2000)
    emp=props(employ)
    print(emp)
    # employ.dispalyEmployee()
    # print("%d" % employ.empCount)
    # employ.displayAge()



