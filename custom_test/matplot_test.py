"""matplot 统计图使用方法"""
import matplotlib.pyplot as plt
import csv


"""
@desc:折线图 坐标轴绘制
@date 2018-01-18
@author: walter
"""
def plot():
    x = [1,2,3]
    y = [5,7,4]
    x2 = [1,2,3]
    y2 = [10,14,12]
    # 画折线
    plt.plot(x, y, label='First Line')
    plt.plot(x2, y2, label='Second Line')
    # X轴标签
    plt.xlabel('Plot Number')
    # Y轴标签
    plt.ylabel('Important var')
    # 标题
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    # 图像显示
    plt.show()


"""
@desc:绘制条形图
@date: 2018-01-18
@author:walter
"""
def bar_plot():
    plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Example one", color='b')
    plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example two", color='g')
    plt.legend()
    plt.xlabel('bar number')
    plt.ylabel('bar height')
    plt.title('Epic Graph\nAnother Line! Whoa')
    plt.show()


"""
@desc:绘制条形图
@date: 2018-01-18
@author:walter
"""
def bar_plot2():
    population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
    bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
    plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()


"""
@desc:绘制散点图
@date: 2018-01-18
@author:walter
"""
def scatter_plot():
    x = [1,2,3,4,5,6,7,8]
    y = [5,2,4,2,1,4,5,2]
    plt.scatter(x,y, label='skitscat', color='k', s=25, marker="o")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()



"""
@desc:绘制堆叠图
@date: 2018-01-18
@author:walter
"""
def stackplot():
    days = [1,2,3,4,5]
    sleeping = [7,8,6,11,7]
    eating =   [2,3,4,3,2]
    working =  [7,8,7,2,2]
    playing =  [8,5,7,8,13]
    plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting Graph\nCheck it out')
    plt.show()

"""
@desc:绘制堆叠图
@date: 2018-01-18
@author:walter
"""
def stackplot2():
    days = [1,2,3,4,5]

    sleeping = [7,8,6,11,7]
    eating =   [2,3,4,3,2]
    working =  [7,8,7,2,2]
    playing =  [8,5,7,8,13]


    plt.plot([],[],color='m', label='Sleeping', linewidth=5)
    plt.plot([],[],color='c', label='Eating', linewidth=5)
    plt.plot([],[],color='r', label='Working', linewidth=5)
    plt.plot([],[],color='k', label='Playing', linewidth=5)

    plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()

"""
@desc:绘制饼图
@date: 2018-01-18
@author:walter
"""
def pieplot():
    slices = [7,2,2,13]
    activities = ['sleeping','eating','working','playing']
    cols = ['c','m','r','b']

    plt.pie(slices,
            labels=activities,
            colors=cols,
            startangle=90,
            shadow= True,
            explode=(0,0.1,0,0),
            autopct='%1.1f%%')

    plt.title('Interesting Graph\nCheck it out')
    plt.show()

"""
@desc:从文件中获取数据进行图形绘制
@date: 2018-01-18
@author:walter
"""
def pieplot_fromfile():
    x = []
    y = []

    with open('example.txt','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(int(row[0]))
            y.append(int(row[1]))

    plt.plot(x,y, label='Loaded from file!')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()



if __name__=="__main__":
    print("开始")
    # plot()
    # bar_plot()
    bar_plot2()
    # scatter_plot()
    # stackplot()
    # stackplot2()
    # pieplot()
    # pieplot_fromfile()