"""numpy模块使用说明"""

#引入numpy包
import numpy as np

def numpy_func():
    #创建二维数组
    print("==初始化矩阵==np_a=np.array([[1,2,3],[4,5,6]])")
    np_a=np.array([[1,2,3],[4,5,6]])
    print(np_a)

    #把数组np_a转换为3行2列
    print("==把数组np_a转换为3行2列==np_a.reshape(3,2)")
    print(np_a.reshape(3,2))

    #转置矩阵
    print("==转置矩阵==np_a.transpose()")
    print(np_a.transpose())

    #求和
    print("==axis=0时对数组np_a的列求和，axis=1时对数组np_a的行求和==np_a.sum(axis=0)")
    print(np_a.sum(axis=0))

    print("==axis=0时求每列的最大值，axis=1时求每行的最大值==np_a.max(axis=0)")
    print(np_a.max(axis=0))

    print("==axis=0时求每列的最小值，axis=1时求每行的最小值==np_a.min(axis=0)")
    print(np_a.min(axis=0))

    #矩阵的特征值和特征向量
    print("==矩阵的特征值和特征向量==np.mat('3 -2;1 0')")
    A = np.mat('3 -2;1 0')
    print(A)

    print("==矩阵的特征值和特征向量==np.mat('3 -2;1 0')")
    B = np.linalg.eig(A)
    print(B)


# N维数组
def ndarray_func():
    # 创建一个2X3的二维数组
    x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
    print("np.array：",x)
    # 输出 二维数组的类型
    print("type(x)：",type(x))
    # 输出数组的shape
    print("x.shape：",x.shape)
    # 输出数组的类型
    print("x.dtype：",x.dtype)
    # The element of x in the *second* row, *third* column, namely, 6.
    #       0  1   2
    #  0    1  2   3
    #  1    4  5   6
    # x[1, 2]
    print("x[1, 2]：",x[1, 2])

    # 数组切片 切片可以生成数组的视图
    y = x[:,1]
    # y输出为：[2 5]
    print("y：",y)
    print("y[0]：",y[0])


# 构造数组
def constructor_array_func():
    # 构造一个2X2的二维数组
    y = np.ndarray(shape=(2,2), dtype=float, order='F')
    print("y：",y)
    # 构造一个2X2的二维数组
    x = np.array([[1,2],[3,4]])
    print("x：",x)
    # 二维数组转置操作
    x_T = x.T
    print("x.T",x_T)
    # x_T.dtype 获取当前变量类型
    print("x_T.dtype",x_T.dtype)
    # x.flags 内存信息
    print("x.flags",x.flags)
    x = np.arange(1, 7).reshape(2, 3)
    print("x",x)
    # x.flat[3]
    print("x.flat[3]",x.flat[3])
    # 数组的虚部
    x = np.sqrt([1+0j, 0+1j])
    print("x",x)
    # image 数组的虚部
    print("x.imag",x.imag)
    # real 数组的实部
    print("x.real",x.real)
    # 数组中的元素数
    x = np.zeros((3, 5, 2), dtype=np.complex128)
    print("x",x)
    #size 数组中的元素个数
    print("x.size",x.size)
    # 元素相乘prod
    print("xnp.prod(x.shape)",np.prod(x.shape))
    # itemsize 一个数组元素的长度（以字节为单位）。
    x = np.array([1,2,3], dtype=np.float64)
    print("x",x.itemsize)
    # 复数
    x = np.array([1,2,3], dtype=np.complex128)
    print("x",x.itemsize)
    #x.nbytes 数组的元素消耗的总字节数。
    print("x.nbytes",x.nbytes)
    # 数组尺寸数。
    x = np.array([1, 2, 3])
    print("x.ndim",x.ndim)
    #numpy.ndarray.shape 数组维数组。
    print("x.shape",x.shape)
    # numpy.ndarray.base
    x = np.array([1,2,3,4])
    print("x.base",x.base)
    y = x[2:]
    print("y.base",y.base)


# 排序、搜索、计数
def sort_func():
    x = np.array([3, 1, 2])
    print("x ",x)
    # 数组排序
    print("np.sort(a) ",np.sort(x))
    # 多维数组排序
    a = np.array([[1,5,4],[3,2,1]])
    print("x ",a)
    # 数组排序 sort along the last axis
    print("np.sort(a) ",np.sort(a))
    # sort the flattened array
    print(" np.sort(a, axis=None) ", np.sort(a, axis=None))
    #  sort along the first axis
    print(" np.sort(a, axis=0) ", np.sort(a, axis=0))
    # 使用键序列执行间接排序。
    surnames =    ('Hertz',    'Galilei', 'Hertz')
    first_names = ('Heinrich', 'Galileo', 'Gustav')
    ind = np.lexsort((first_names, surnames))
    print("ind",ind)
    rs = [surnames[i] + ", " + first_names[i] for i in ind]
    print("rs",rs)

    # 返回将数组分类的索引 返回索引
    x = np.array([3, 1, 2])
    print("np.argsort(x)",np.argsort(x))
    # 排序后重新赋值到新的数组中
    rs = [x[i] for i in ind]
    print("rs",rs)

    # 返回沿第一个轴排序的数组的副本。
    x = np.array([3, 1, 2])
    print("np.msort(x)",np.msort(x))
    y = np.sort_complex([5, 3, 6, 2, 1])
    print("y",y)

    # numpy.argmax 返回沿轴的最大值的索引
    a = np.arange(6).reshape(2,3)
    print("a",a)
    print("np.argmax(a)",np.argmax(a))

    # numpy.argpartition
    a = np.array([[np.nan, 4], [2, 3]])
    print("np.nanargmax(a)",np.nanargmax(a))

    a = np.arange(6).reshape(2,3)
    print("a",a)
    print("np.argmin(a)",np.argmin(a))

    # 找到非零的数组元素的索引，按元素分组
    x=np.argwhere(x>1)
    print("x",x)
    x=np.where(x>1)
    print("x",x)

    # 查找要插入元素以维持顺序的索引
    x=np.searchsorted([1,2,3,4,5], 3)
    print("x",x)


"""
@desc:统计函数
@date:2018-01-19
@author:Walter
"""
def static_func():
    a = np.arange(4).reshape((2,2))
    print("a",a)
    # 获取最小值
    print("np.amin(a)",np.amin(a))
    # 获取最大值
    print("np.amax(a)",np.amax(a))
    # 沿轴的值范围（最大 - 最小）
    print("np.ptp(a, axis=0)",np.ptp(a, axis=0))
    # 沿指定轴计算数据的第q个百分位数
    print("np.percentile(a, 50)",np.percentile(a, 50))
    # 返回数组元素的中位数。
    a = np.array([[10, 7, 4], [3, 2, 1]])
    print("np.median(a)",np.median(a))
    # 0轴上的中位数
    print("np.median(a, axis=0)",np.median(a, axis=0))
    # 1轴上的中位数
    print("np.median(a, axis=1)",np.median(a, axis=1))
    # 平均数
    data = range(1,5)
    print("data",data)
    print("np.average(data)",np.average(data))
    # 算术平均值
    print("np.mean(data)",np.mean(data))
    # 计算沿指定轴的标准偏差
    print("np.std(data)",np.std(data))
    # 计算沿指定轴的方差
    print("np.var(data)",np.var(data))


"""
@desc:线性代数
@date:2018-01-19
@author:Walter
"""
def linalog_func():
    # 两个数组的点积
    x=np.dot(3, 4)
    print("x",x)

    # 2-D数组，它是矩阵积
    a = [[1, 0], [0, 1]]
    b = [[4, 1], [2, 2]]
    x=np.dot(a, b)
    print("x",x)

    # 向量点积
    a = np.array([1+2j,3+4j])
    b = np.array([5+6j,7+8j])
    x=np.vdot(a, b)
    print("x",x)
    x=np.vdot(b, a)
    print("x",x)

    # 两个数组的内积
    a = np.array([1,2,3])
    b = np.array([0,1,0])
    x=np.inner(a, b)
    print("x",x)

    # 计算两个向量的外积
    a = np.array([1+2j,3+4j])
    b = np.array([5+6j,7+8j])
    x=np.outer(a, b)
    print("x",x)

    # 两个数组的矩阵乘积
    a = [1, -1]
    b = [1, 2]
    x=np.matmul(a, b)
    print("x",x)

#main函数
if __name__=="__main__":
    print("开始")
    # numpy_func()
    # ndarray_func()
    # constructor_array_func()
    # sort_func()
    # static_func()
    linalog_func()
    print("结束")
