import numpy as np
import pandas as pd
from pandas import Series,DataFrame

#机器学习的普通线性模型、岭回归模型、lasso模型
from sklearn.linear_model import LinearRegression,Ridge,Lasso
#模型效果评估
from sklearn.metrics import r2_score
#导入机器学习相关的数据集
import sklearn.datasets as datasets
import matplotlib.pyplot as plt #画图

##数据输出

"""
@desc:分别用普通线性回归、岭回归、Lasso回归对boston房价进行预测，比较效果
@date:2018-01-23
@author:Walter
"""
def lasso_ridge_line():

    #从datasets模块中导入boston房价数据
    boston = datasets.load_boston()
    data = boston.data
    target=boston.target

    #训练数据
    X_train = data[:480]
    Y_train = target[:480]

    #测试数据
    x_test = data[480:]
    y_true = target[480:]

    # 确定机器学习模型
    line = LinearRegression()
    ridge = Ridge()
    lasso = Lasso()

    # 数据训练
    line.fit(X_train,Y_train)
    ridge.fit(X_train,Y_train)
    lasso.fit(X_train,Y_train)

    # 预测数据
    line_y_pre=line.predict(x_test)
    ridge_y_pre=ridge.predict(x_test)
    lasso_y_pre=lasso.predict(x_test)

    # 画图
    plt.plot(y_true,label='True')
    plt.plot(line_y_pre,label='Line')
    plt.plot(ridge_y_pre,label='Ridge')
    plt.plot(lasso_y_pre,label='Lasso')
    plt.legend()
    plt.show()

    # 训练处的模型进行准确性判断
    line_score=r2_score(y_true,line_y_pre)
    print("线性模型预测结果评分=",line_score)
    ridge_score=r2_score(y_true,ridge_y_pre)
    print("ridge模型预测结果评分=",ridge_score)
    lasso_score=r2_score(y_true,lasso_y_pre)
    print("lasso模型预测结果评分=",lasso_score)


if __name__=='__main__':
    print("开始")
    lasso_ridge_line()
