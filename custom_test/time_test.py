import time

def time_init():
    # 获取时间戳
    t=time.time()
    print(t)
    # 将当前时间戳转换为元组
    tuple = time.localtime(t)
    print(tuple)
    # 通过元组中的定义来获取元组中的内容
    print(tuple.tm_year)
    # 元组转换为时间戳，毫秒级别将会被忽略
    tm=time.mktime(tuple)
    print(tm)
    #格式化时间元组
    t=time.time()
    tuple = time.localtime(t)
    # 格式化时间元组为 年月日 时分秒
    # tm_str=time.strftime("%Y%m%d %H:%M:%S",tuple)
    # 一年中第几天
    tm_str=time.strftime("%j",tuple)
    print(tm_str)

def get_clock():
    # 获取CPU运行时间来获取比较精确的运行秒数
    print("start1:",time.clock())
    time.sleep(5)
    print("end1:",time.clock())
    time.sleep(5)
    print("end2",time.clock())


def time_format():
    #格式化时间元组
    t=time.time()
    tuple = time.localtime(t)
    # 格式化时间元组为 年月日 时分秒
    tm_str=time.strftime("%Y%m%d %H:%M:%S",tuple)
    # 将字符串转换为时间元组
    tup2=time.strptime(tm_str,"%Y%m%d %H:%M:%S")
    print(tup2)

if __name__ =="__main__":
    # time_init()
    # get_clock()
    time_format()