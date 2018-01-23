"""
@desc:逻辑回归
@date:2018-01-23
@author:Walter
"""
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
import sklearn
from sklearn.linear_model import LogisticRegressionCV,LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model.coordinate_descent import ConvergenceWarning


"""
入口
"""
if __name__=='__main__':
    print("开始")
    path="breast-cancer-wisconsin.data"

    names=["id","Clump Thickness"]
    df = pd.read_csv(path,header=None,names=names)
    print(df.head())
    datas = df.replace('?',np.nan)

