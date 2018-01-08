"""pandas框架使用说明"""
import pandas as pd
import numpy as np


# pandas开始
def pandas_func():
    #创建对象：序列、数据帧
    #序列
    s = pd.Series([1,3,5,np.nan,6,8])
    print("s",s)

    #
    dates = pd.date_range('20130101', periods=6)
    print("dates",dates)

    #数据帧
    df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
    print("df",df)
    #数据帧
    df2 = pd.DataFrame({ 'A' : 1.,
                         'B' : pd.Timestamp('20130102'),
                         'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                         'D' : np.array([3] * 4,dtype='int32'),
                         'E' : pd.Categorical(["test","train","test","train"]),
                         'F' : 'foo' })
    print("df2",df2)

    #查看数据帧中的数据
    #df.head() 前n行数据
    print("df.head()",df.head(1))

    #查看数据帧中的数据
    #df.tail() 后n行数据
    print("df.tail()",df.tail(1))

    #查看数据帧中的数据
    # df.index
    print("df.index",df.index)

    #查看数据帧中的数据
    # df.columns
    print("df.columns",df.columns)

    #查看数据帧中的数据
    # df.values
    print("df.values",df.values)

    #查看数据帧中的数据
    #  df.describe()
    print(" df.describe()", df.describe())

    #查看数据帧中的数据
    # df.T
    print("df.T",df.T)

    #查看数据帧中的数据
    # df.sort_index(axis=1, ascending=False)
    print("df.sort_index(axis=1, ascending=False)",df.sort_index(axis=1, ascending=False))

    #查看数据帧中的数据
    # df.sort_values(by='B')
    print("df.sort_values(by='B')",df.sort_values(by='B'))

    #选择 获取数据
    print("df['A']",df["A"]);

    #选择 获取数据 df[0:3]
    print("df[0:3]", df[0:3]);

    #选择 获取数据 df['20130102':'20130104']
    print("df['20130102':'20130104']", df['20130102':'20130104']);

    #选择 获取数据 df.loc[dates[0]]
    print("df.loc[dates[0]]", df.loc[dates[0]]);

    #选择 获取数据  df.loc[:,['A','B']]
    print(" df.loc[:,['A','B']]", df.loc[:,['A','B']]);

    #选择 df.loc['20130102':'20130104',['A','B']]
    print("df.loc['20130102':'20130104',['A','B']]", df.loc['20130102':'20130104',['A','B']]);

    #选择 df.loc['20130102',['A','B']]
    print("df.loc['20130102',['A','B']]", df.loc['20130102',['A','B']]);

    #选择 df.loc[dates[0],'A']
    print("df.loc[dates[0],'A']",df.loc[dates[0],'A']);

    #选择 df.iloc[1,1]
    print("df.iloc[1,1]",df.iloc[1,1]);

    #选择 df.iat[1,1]
    print("df.iat[1,1]",df.iat[1,1]);

    #布尔索引 df[df.A > 0]
    print("df[df.A > 0]",df[df.A > 0]);



#入口
if __name__=="__main__":
    print("开始")
    pandas_func()
    print("结束")
