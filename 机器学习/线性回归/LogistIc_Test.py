import pandas as pd
import numpy as np
import time
import sklearn
import matplotlib as mpl
import matplotlib.pyplot as plt #画图
from sklearn.linear_model import LinearRegression,Lasso,Ridge #线性回归
from sklearn.model_selection import train_test_split #数据分割
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib #模型保存
from sklearn.pipeline import Pipeline #导入管道包
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


"""
1.date: Date in format dd/mm/yyyy 
2.time: time in format hh:mm:ss 
3.global_active_power: household global minute-averaged active power (in kilowatt) 
4.global_reactive_power: household global minute-averaged reactive power (in kilowatt) 
5.voltage: minute-averaged voltage (in volt) 
6.global_intensity: household global minute-averaged current intensity (in ampere) 
7.sub_metering_1: energy sub-metering No. 1 (in watt-hour of active energy). It corresponds to the kitchen, containing mainly a dishwasher, an oven and a microwave (hot plates are not electric but gas powered). 
8.sub_metering_2: energy sub-metering No. 2 (in watt-hour of active energy). It corresponds to the laundry room, containing a washing-machine, a tumble-drier, a refrigerator and a light. 
9.sub_metering_3: energy sub-metering No. 3 (in watt-hour of active energy). It corresponds to an electric water-heater and an air-conditioner.

需求：
模型：时间与功率的关系

"""
def time_dy():
    #数据集地址
    path='household_power_consumption_1000.txt'

    #数据集列名
    names=["Date","Time","Global_active_power","Global_reactive_power","Voltage","Global_intensity","Sub_metering_1","Sub_metering_2","Sub_metering_3"]

    #read_csv（数据，分割符号）读取数据
    df = pd.read_csv(path,sep=";")

    #打印前五行数据
    print(df.head())

    #如果是问号，改为空值
    new_df = df.replace('?',np.nan)

    #处理空值
    datas = new_df.dropna(how='any')

    #看所有的变量值

    #获取X,Y变量，讲时间转换为数值型的连续变量
    X=datas[names[0:2]]
    X=X.apply(lambda x :pd.Series(date_format(x)),axis=1)

    Y=datas[names[2]]

    # print(X.head(5))
    # print(Y.head(5))
    #对数据集进行训练，测试集划分
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

    #数据标准化
    ss=StandardScaler()
    X_train=ss.fit_transform(X_train)
    X_test=ss.transform(X_test)

    #训练模型
    lr=LinearRegression()
    lr.fit(X_train,Y_train)

    #训练完之后，给训练效果打分
    print("准确率：",lr.score(X_train,Y_train))

    #预测y值
    y_predict=lr.predict(X_test)

    #保存模型
    joblib.dump(ss,"data_ss.model")
    joblib.dump(lr,"data_lr.model")
    #加载模型
    joblib.load("data_ss.model")
    joblib.load("data_lr.model")

    #设置字符集，防止中文乱码
    mpl.rcParams["font.sans-serif"]=[u'simHei']
    mpl.rcParams["axes.unicode_minus"]=False

    #预测值与实际值画图比较
    t=np.arange(len(X_test))
    plt.figure(facecolor='w')
    plt.plot(t,Y_test,"r-",linewidth=2,label=u'真实值')
    plt.plot(t,y_predict,"g-",linewidth=2,label=u'真实值')
    plt.legend(loc='lower right')
    plt.title(u'线性回归预测时间与功率之间的关系',fontsize=20)
    plt.grid(b=True)
    plt.show()

#创建一个时间字符串格式化
def date_format(dt):
    t = time.strptime(' '.join(dt),'%d/%m/%Y %H:%M:%S')
    return (t.tm_year,t.tm_mon,t.tm_mday,t.tm_hour,t.tm_min,t.tm_sec)



def time2gl():
    # time_dy()
    print("开始")

    #时间与电压的关系
    #数据集地址
    path='household_power_consumption_1000.txt'

    #数据集列名
    names=["Date","Time","Global_active_power","Global_reactive_power","Voltage","Global_intensity","Sub_metering_1","Sub_metering_2","Sub_metering_3"]

    #read_csv（数据，分割符号）读取数据
    df = pd.read_csv(path,sep=";")

    #如果是问号，改为空值
    new_df = df.replace('?',np.nan)

    #处理空值
    datas = new_df.dropna(how='any')

    #看所有的变量值

    #获取X,Y变量，讲时间转换为数值型的连续变量
    X=datas[names[0:2]]
    X=X.apply(lambda x :pd.Series(date_format(x)),axis=1)

    #获取电压Y
    Y=datas[names[4]]

    # print(X.head(5))
    # print(Y.head(5))
    #对数据集进行训练，测试集划分
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

    #数据标准化
    ss=StandardScaler()
    X_train=ss.fit_transform(X_train)
    X_test=ss.transform(X_test)

    #训练模型
    lr=LinearRegression()
    lr.fit(X_train,Y_train)

    #训练完之后，给训练效果打分
    # print("准确率：",lr.score(X_train,Y_train))
    print("准确率：",lr.score(X_test,Y_test))

    #预测y值
    y_predict=lr.predict(X_test)

    #保存模型
    joblib.dump(ss,"data_ss1.model")
    joblib.dump(lr,"data_lr1.model")
    #加载模型
    joblib.load("data_ss1.model")
    joblib.load("data_lr1.model")

    #设置字符集，防止中文乱码
    mpl.rcParams["font.sans-serif"]=[u'simHei']
    mpl.rcParams["axes.unicode_minus"]=False

    #预测值与实际值画图比较
    t=np.arange(len(X_test))
    plt.figure(facecolor='w')
    plt.plot(t,Y_test,"r-",linewidth=2,label=u'真实值')
    plt.plot(t,y_predict,"g-",linewidth=2,label=u'真实值')
    plt.legend(loc='lower right')
    plt.title(u'线性回归预测时间与电压之间的关系',fontsize=20)
    plt.grid(b=True)
    plt.show()






if __name__=="__main__":
    # time_dy()
    print("开始")

    #时间与电压的关系
    #数据集地址
    path='household_power_consumption_1000.txt'

    #数据集列名
    names=["Date","Time","Global_active_power","Global_reactive_power","Voltage","Global_intensity","Sub_metering_1","Sub_metering_2","Sub_metering_3"]

    #read_csv（数据，分割符号）读取数据
    df = pd.read_csv(path,sep=";")

    #如果是问号，改为空值
    new_df = df.replace('?',np.nan)

    #处理空值
    datas = new_df.dropna(how='any')

    #时间与电压的关系（linear多项式）PolynomialFeatures
    models=[Pipeline([('poly',PolynomialFeatures()),
            ('linear',LinearRegression())])
    ]
    model = models[0]
    #获取x,y变量，并将时间变量转换为数值型连续型的
    X=datas[names[0:2]]
    X=X.apply(lambda x :pd.Series(date_format(x)),axis=1)
    #获取电压Y
    Y=datas[names[4]]

    #对数据集进行划分
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

    #数据标准化
    ss=StandardScaler()
    X_train=ss.fit_transform(X_train)
    X_test=ss.transform(X_test)

    #模型训练
    t=np.arange(len(X_test))
    N=5
    d_pool=np.arange(1,N,1)
    m=d_pool.size
    #定义颜色
    clrs=[]
    for c in np.linspace(16711680,255,m):
        clrs.append('#%06x'%int(c))
    line_width=3

    plt.figure(figsize=(12,6),facecolor='w')
    # for i,d in enumerate(d_pool):
    #     plt.subplot(N-1,1,i+1)
    #     # plt.plot(t,Y_test,'r-',linewidth=2,label=u'真实值',ms=10,zoder=N)
    #     # plt.plot(t,Y_test,'r-',label=u'真实值',ms=10,zoder=N)
    #     #设置多项式的阶
    #     model.set_params(degree=d)
    #     model.fit(X_train,Y_train)
    #     lin=model.get_params('Linear')['Linear']
    #     output=u'%d阶,系数为:'%d
    #     print(output,lin.coef_.ravel())

    for count, degree in enumerate(d_pool):
        model = make_pipeline(PolynomialFeatures(degree), Ridge())
        model.fit(X_train, Y_train)
        y_hat = model.predict(X_test)
        plt.plot(t, y_hat, color=clrs[count], linewidth=line_width,
                 label="degree %d" % degree)

        # s=model.score(X_test,Y_test)
        # z=N-1 if (d==2) else 0
        # label=u'%d阶,准确率=%.3f'%(d,s)#
        # plt.legend(loc='upper left')
        # plt.grid(True)
        # plt.ylabel(u'%d阶结果'%d,fontsize=12)

        plt.legend(loc='lower right')
        # plt.subtitle(u'线性回归时间与电压之间多项式关系')
        plt.grid(b=True)
        plt.show()





