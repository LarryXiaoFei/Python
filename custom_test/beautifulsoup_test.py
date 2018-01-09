"""BeautifulSoup使用说明"""
from bs4 import BeautifulSoup
from urllib import request


#BeautifulSoup 使用方法
def beautifulsoup_func():
    # 初始化html
    html_doc = '<html><head><title>The Dormouses story</title></head><body><p class="title">'
    html_doc=html_doc+ '<b>The Dormouse story</b></p><p class="story">Once upon a time there were three little sisters; and their names were'
    html_doc=html_doc+ '<a class="sister" href="http://example.com/elsie" id="link1"> Elsie; and they lived at the bottom of a well.</p><p class="story">...</p></body></html>'

    # 网络获取
    response = request.urlopen("http://www.yiibai.com/")
    html_doc = response.read();

    # 创建BeautifulSoup对象
    soup = BeautifulSoup(html_doc)
    # 按照标准缩进格式输出
    print("soup.prettify()",soup.prettify())

    #soup.title 获取Html的标题
    print("soup.title",soup.title)

    # soup.title.name 获取Html的标题
    print("soup.title.name",soup.title.name)

    # soup.title.string 获取Html的标题
    print("soup.title.string",soup.title.string)

    # soup.title.parent.name 获取Html的标题
    print("soup.title.parent.name",soup.title.parent.name)

    # soup.p 获取p标签
    print("soup.p",soup.p)


    # soup.a 获取p标签
    print("soup.a",soup.a)

    # soup.find_all('a') 获取p标签
    # print("soup.find_all('a')",soup.find_all('a'))
    # 解析获取目标数据：url地址、邮箱地址、电话号码...
    hrefs = ""
    for link in soup.find_all('a'):
        href = link.get("href")
        hrefs = hrefs + href +"|"

    #数据写入到文件/数据库
    file = open("links.txt", "r+")
    file.write(hrefs)
    file.close()
    hrefs

    return ;



if __name__=="__main__":
    print("开始")
    beautifulsoup_func()
    print("结束")