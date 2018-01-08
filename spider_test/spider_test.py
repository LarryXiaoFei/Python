# 引入 urllib 模块
# 引入 chardet 模块
from urllib import request
import chardet
from urllib import parse
import json
from urllib import error
from http import cookiejar


def urllib_simple_test():
    """
    @desc:urllib获取网络数据
    @date:2018-01-08
    @author:walter
    """
    print("urllib开始...")
    response = request.urlopen("http://fanyi.baidu.com")
    html = response.read()
    charset = chardet.detect(html)
    html = html.decode("utf-8")
    print("html",html)
    print("charset",charset)


def urllib_open_test():
    """
    @desc:urllib获取网络数据
    @date:2018-01-08
    @author:walter
    """
    #对应上图的Request URL
    Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
    #创建Form_Data字典，存储上图的Form Data
    Form_Data = {}
    Form_Data['type'] = 'AUTO'
    Form_Data['i'] = 'Jack'
    Form_Data['doctype'] = 'json'
    Form_Data['xmlVersion'] = '1.8'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['ue'] = 'ue:UTF-8'
    Form_Data['action'] = 'FY_BY_CLICKBUTTON'
    #使用urlencode方法转换标准格式
    data = parse.urlencode(Form_Data).encode('utf-8')
    #传递Request对象和转换完格式的数据
    response = request.urlopen(Request_URL,data)
    #读取信息并解码
    html = response.read().decode('utf-8')
    #使用JSON
    translate_results = json.loads(html)
    #找到翻译结果
    translate_results = translate_results['translateResult'][0][0]['tgt']
    #打印翻译信息
    print("翻译的结果是：%s" % translate_results)


def urlerro_test():
    #一个不存在的连接
    url = "http://www.iloveyou.com/"
    req = request.Request(url)
    try:
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        print(html)
    except error.URLError as e:
        print(e.reason)

def UserAgent_test():
    #以CSDN为例，CSDN不更改User Agent是无法访问的
    url = 'http://www.csdn.net/'
    head = {}
    #写入User Agent信息
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    #创建Request对象
    req = request.Request(url, headers=head)
    #传入创建好的Request对象
    response = request.urlopen(req)
    #读取响应信息并解码
    html = response.read().decode('utf-8')
    #打印信息
    print(html)

def UserAgentTwo_test():
    #以CSDN为例，CSDN不更改User Agent是无法访问的
    url = 'http://www.csdn.net/'
    #创建Request对象
    req = request.Request(url)
    #传入headers
    req.add_header('User-Agent', 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19')
    #传入创建好的Request对象
    response = request.urlopen(req)
    #读取响应信息并解码
    html = response.read().decode('utf-8')
    #打印信息
    print(html)

def hideIp_test():
    #访问网址
    url = 'http://www.whatismyip.com.tw/'
    #这是代理IP
    proxy = {'http':'122.114.31.177:808'}
    #创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    #创建Opener
    opener = request.build_opener(proxy_support)
    #添加User Angent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    #安装OPener
    request.install_opener(opener)
    #使用自己安装好的Opener
    response = request.urlopen(url)
    #读取相应信息并解码
    html = response.read().decode("utf-8")
    #打印信息
    print(html)

def cookie_test():
    #设置保存cookie的文件，同级目录下的cookie.txt
    filename = 'cookie.txt'
    #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = cookiejar.MozillaCookieJar(filename)
    #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler=request.HTTPCookieProcessor(cookie)
    #通过CookieHandler创建opener
    opener = request.build_opener(handler)
    #此处的open方法打开网页
    response = opener.open('http://www.baidu.com')
    #保存cookie到文件
    cookie.save(ignore_discard=True, ignore_expires=True)

def cookie_read():
    #设置保存cookie的文件的文件名,相对路径,也就是同级目录下
    filename = 'cookie.txt'
    #创建MozillaCookieJar实例对象
    cookie = cookiejar.MozillaCookieJar()
    #从文件中读取cookie内容到变量
    cookie.load(filename, ignore_discard=True, ignore_expires=True)
    #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler=request.HTTPCookieProcessor(cookie)
    #通过CookieHandler创建opener
    opener = request.build_opener(handler)
    #此用opener的open方法打开网页
    response = opener.open('http://www.baidu.com')
    #打印信息
    print(response.read().decode('utf-8'))

def cookie_main():
    #登陆地址
    login_url = 'http://www.jobbole.com/wp-admin/admin-ajax.php'
    #User-Agent信息
    user_agent = r'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
    #Headers信息
    head = {'User-Agnet': user_agent, 'Connection': 'keep-alive'}
    #登陆Form_Data信息
    Login_Data = {}
    Login_Data['action'] = 'user_login'
    Login_Data['redirect_url'] = 'http://www.jobbole.com/'
    Login_Data['remember_me'] = '0'         #是否一个月内自动登陆
    Login_Data['user_login'] = '********'       #改成你自己的用户名
    Login_Data['user_pass'] = '********'        #改成你自己的密码
    #使用urlencode方法转换标准格式
    logingpostdata = parse.urlencode(Login_Data).encode('utf-8')
    #声明一个CookieJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    cookie_support = request.HTTPCookieProcessor(cookie)
    #通过CookieHandler创建opener
    opener = request.build_opener(cookie_support)
    #创建Request对象
    req1 = request.Request(url=login_url, data=logingpostdata, headers=head)

    #面向对象地址
    date_url = 'http://date.jobbole.com/wp-admin/admin-ajax.php'
    #面向对象
    Date_Data = {}
    Date_Data['action'] = 'get_date_contact'
    Date_Data['postId'] = '4128'
    #使用urlencode方法转换标准格式
    datepostdata = parse.urlencode(Date_Data).encode('utf-8')
    req2 = request.Request(url=date_url, data=datepostdata, headers=head)
    try:
        #使用自己创建的opener的open方法
        response1 = opener.open(req1)
        response2 = opener.open(req2)
        html = response2.read().decode('utf-8')
        index = html.find('jb_contact_email')
        #打印查询结果
        print('联系邮箱:%s' % html[index+19:-2])

    except error.URLError as e:
        if hasattr(e, 'code'):
            print("HTTPError:%d" % e.code)
        elif hasattr(e, 'reason'):
            print("URLError:%s" % e.reason)

if __name__=="__main__":
    print("开始")
    cookie_main()
    print("结束")