#!/usr/bin/python3


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


#入口
if __name__=="__main__":
    print("开始")
    string_func()
    print("结束")

