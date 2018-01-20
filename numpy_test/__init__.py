
#引入numpy包
import numpy as np

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

