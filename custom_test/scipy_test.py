"""
@desc:scipy包相关练习code
@date:2018-01-31
@author:Walter
"""
#导入图片模块
#导入统计模块
from scipy import stats,misc,linalg
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


"""
@desc:初始化操作
@date:2018-01-31
@author:Walter
"""
def scipy_init():
    print("scipy_init")
    # 随机产生30个随机数
    fs_meetsig = np.random.random(30)
    # 进行排序
    fs_xk = np.sort(fs_meetsig)
    print(fs_xk)
    #
    fs_pk = np.ones_like(fs_xk) / len(fs_xk)
    print(fs_pk)
    # 中的参数表示随机变量x和其对应的概率
    fs_rv_dist = stats.rv_discrete(name='fs_rv_dist', values=(fs_xk, fs_pk))
    print(fs_rv_dist.cdf(fs_xk))
    # 绘图
    plt.plot(fs_xk, fs_rv_dist.cdf(fs_xk), 'b-', ms=12, mec='r', label='friend')
    plt.show()


"""
@desc:读取图片信息
@date:2018-01-31
@author:Walter
"""
def read_img():
    print("读取图片信息")
    data=misc.imread('scipy_tets.png')
    print(data)

"""
@desc:特殊函数scipy.special
@date:2018-01-31
@author:Walter
"""
def linalg_init():
    print("读取图片信息")
    arr = np.array([[1, 2],[3, 4]])
    # 函数计算方阵的行列式
    x=linalg.det(arr)
    print(x)
    # py.linalg.inv()`函数计算方阵的逆：
    iarr = linalg.inv(arr)
    print(iarr)

if __name__=="__main__":
    print("开始")
    # scipy_init()
    # read_img()
    linalg_init()