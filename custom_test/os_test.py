import os, sys


"""
@desc:测试当前用户是否能够访问改文件
@date:2018-01-18
@author:walter
"""
def os_test():
    #测试调用用户是否拥有指定路径访问权限
    ret = os.access("links.txt", os.F_OK)
    print ("F_OK - return value %s"% ret)

    path="C:/Users/Walter/workspace_xianyang/python"
    # Now change the directory
    os.chdir(path)
    # Check current working directory.
    retval = os.getcwd()

    print ("Directory changed successfully %s" % retval)




"""
@desc:listdir遍历
@date:2018-01-18
@author:walter
"""
def listdir_test():
    #遍历目录下所有文件
    path="C:/Users/Walter/workspace_xianyang/python/"
    #Return a list containing the names of the files in the directory
    #返回指定路径下所有文件的文件名
    files = os.listdir(path)
    count = len(files)
    print ("文件总数 %s" % count)

    for file in files:
        print(file)
        print(type(file))
        if file=='python.iml':
            f = open(path+file)
            line = f.readline()
            while line:
                line = f.readline()
                print(line)





if __name__=="__main__":
    print("开始")
    # os_test()
    listdir_test()