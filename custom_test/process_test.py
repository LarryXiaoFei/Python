import time
import multiprocessing

# 创建函数并执行
def worker_1(interval):
    n=5
    while n>1:
        print("worker_1",n)
        time.sleep(interval)
        n=n-1


# 创建函数并执行
def worker_2(interval):
    n=5
    while n>1:
        print("worker_2",n)
        time.sleep(interval)
        n=n-1

# 创建函数并执行
def worker_3(interval):
    n=5
    while n>1:
        print("worker_3",n)
        time.sleep(interval)
        n=n-1


"""
入口函数
"""
if __name__=="__main__":
    print("")
    p1=multiprocessing.Process(target=worker_1(3))
    p2=multiprocessing.Process(target=worker_2(4))
    p3=multiprocessing.Process(target=worker_3(5))
    p1.start()
    p2.start()
    p3.start()