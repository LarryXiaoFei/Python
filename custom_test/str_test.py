#!/usr/bin/python3
#math 引入math模块
#random 引入随机数模块
#time 引入时间模块
#calendar 引入日历模块
import math
import random
import time
import calendar

"""
@created:walter
@date:2018-01-08
@desc:string_test
"""


def init_str():
    """
    @desc:init string and how to get the words
    """
    param1 = "Hello Python"
    param2 = "Python Programming"
    print(print(param1[0]))
    print(print(param2[1:5]))
    return


def string_func():
    """string func test"""
    param1 = "hello python"

    #首字母大写
    print("hello python : str.capitalize()",param1.capitalize());
    #计算字符传长度
    print("hello python : len",len(param1));
    #以当前字符串为中点两边添加指定字符
    print("hello python : str.center()",param1.center(len(param1)+5,"*"));
    #计算当前字段中包含了多少个指定字符传
    print("hello python : param1.count(1) ",param1.count("h",0,len(param1)));
    #编码字符串
    print("hello python : param1.encode() ",param1.encode("utf8","strict"));
    param2 = param1.encode("utf8","strict")
    #解码字符
    print("hello python : param1.decode() ",param2.decode("utf8","strict"));
    #是否以指定字符串结束
    print("hello python : param1.endswith() ",param1.endswith("h",0,len(param1)));
    #是否以指定字符串开始
    print("hello python : param1.startswith() ",param1.startswith("h",0,len(param1)));
    param1 = "hello\t python"
    #拓展制表符
    print("hello python : param1.expandtabs() ",param1.expandtabs(16));
    #查找指定字符
    print("hello python : param1.find() ",param1.find("p",6,len(param1)));
    #是否包含字母数字
    print("hello python : param1.isalnum() ",param1.isalnum());
    #是否只包含字母
    print("hello python : param1.isalpha() ",param1.isalpha());
    #是否只包含数字
    print("hello python : param1.isdigit() ",param1.isdigit());
    #是否都为小写字母
    # print("hello python : param1.tolower() ",param1.tolower());
    #是否都为空格字符
    print("hello python : param1.isspace() ",param1.isspace());
    #是否都为标题字符 Xxxx Mnns
    print("hello python : param1.istitle() ",param1.istitle());
    #左侧补上指定字符ljust
    print("hello python : param1.ljust() ",param1.ljust(len(param1)+4,"*"));
    #右侧补上指定字符rjust
    print("hello python : param1.rjust() ",param1.rjust(len(param1)+4,"+"));
    #字母大写
    print("hello python : param1.upper() ",param1.upper());
    param1="HELLO WORLD"
    #字母小写
    print("hello python : param1.lower() ",param1.lower());
    #lstrip 左边字符修剪
    param1="&HELLO WORLD&"
    print("hello python : param1.lstrip() ",param1.lstrip("&"));
    #max 最大字符
    param1="&HELLO WORLD&"
    print("hello python : max ",max(param1));
    #min 最小字符
    param1="HELLO"
    print("hello python : max ",min(param1));
    #replace 替换
    param1="HELLO"
    print("hello python : replace ",param1.replace("L","*"));
    #rfind 查找第一个索引
    param1="HELLLO"
    print("hello python : replace ",param1.rfind("L",0,len(param1)));
    #rindex 查找最后一个索引
    param1="HELLLO"
    print("hello python : replace ",param1.rindex("L",0,len(param1)));

    #split 分割
    param1="HELLO|WORLD"
    print("hello python : replace ",param1.split("1"));


#数字函数
def num_func():
    """
    @desc:number calculate functions in this module
    """
    ##数学函数##
    #abs绝对值
    print("abs(-1):",abs(-1));
    #ceil 不小于x的最小整数
    print("math.ceil(1.2):",math.ceil(1.2));
    #exp e
    print("math.exp(1):",math.exp(1));
    #ceil 不大于x的最小整数
    print("math.floor(1.2):",math.floor(1.2));
    #log 对数函数
    print("math.log(4,2):",math.log(4,2));
    #log10 对数函数
    print("math.log10(100):",math.log10(100));
    #max(100,200,300) 最大数
    print("max(100,200,300):",max(100,200,300));
    #min(100,200,300) 最小数
    print("min(100,200,300):",min(100,200,300));
    #modf 分离整数和小数
    print("math.modf(40.01):",math.modf(40.01));
    #pow 指数函数
    print("math.pow(4,2):",math.pow(4,2));
    #round 四舍五入
    print("round(4.2545,3):",round(4.2545,3));
    #sqrt 算数平方根
    print("sqrt(4):",math.sqrt(4));

    ##随机数函数##
    #choice 随机返回List中的数
    print("choice([1,2,3,4]):",random.choice([1,2,3,4]));

    ##三角函数##
    #sin 正弦函数
    print("math.sin(math.pi/3):",math.sin(math.pi/3));
    #cos 余弦函数
    print("math.cos(math.pi/3):",math.cos(math.pi/3));


    ##数学常数##
    #math.pi pi
    print("math.pi:",math.pi);

    return ;


#列表list
def list_func():
    """
    @desc:define a function that provides some functions usage about list of python
    """
    #定义列表
    param = ["张三","李四","王五"];
    print('["张三","李四","王五"]',param)
    #访问列表
    print('param[0]',param[0])
    print('param[1:2]',param[1:])
    #新增
    param.append("马六")
    print('param',param)
    #修改
    param[3] = "无名"
    print('param',param)
    # 删除
    param.remove("无名")
    print('param',param)
    #len
    print("len(param)",len(param))

    #other functions you can search website ...

    return;


#字典 dictory
def dict_func():
    #字典的定义及访问
    dict = {"Name":"张三","Age":15}
    print("dict",dict)
    print("dict",dict["Name"])
    #更新字典值
    dict["Name"] = "王五"
    print("dict",dict["Name"])
    #删除字典
    del dict["Name"]
    print("dict",dict)
    #items
    print("dict.items()",dict.items())
    #keys
    print("dict.keys()",dict.keys())
    #values
    print("dict.values()",dict.values())

    return ;


#元组
def tuple_func():
    #元组的定义及访问
    tuple = (1,2,3,4,4,5)
    print("tuple",tuple)
    print("tuple[0]",tuple[0])

    return ;

#日期与时间
def time_func():
    #时间元组
    print("time.time()",time.time());
    print("time.localtime()",time.localtime());
    #获取当前时间及时间格式化
    localtime = time.asctime(time.localtime(time.time()))
    print("localtime",localtime)
    #获取一个月的日历
    print("calendar.month(2018,1)",calendar.month(2018,1));
    return ;



#while循环
def while_func():
    count=0;
    while(count<9):
        count=count+1
        print(count)
    else:
        print("结束当前count为",count);
    return ;


#for循环
def for_func():
    nums = [1,2,3,4,5,6,7];
    for num in nums:
        if num%2==0:
            print("偶数",num)
        else:
            print("奇数",num)
    else:
        print("遍历结束")
    return ;


#异常Exception
def exception_func():
    try:
        print("开始2/0")
        print(2/0)
    except(Exception):
        print("except异常")
    finally:
        print("finally结束")
    return ;




#入口
if __name__=="__main__":
    print("开始")
    # string_func()
    # num_func()
    # list_func()
    # dict_func()
    # tuple_func()
    # time_func()
    # while_func()
    # for_func()
    exception_func()
    print("结束")

