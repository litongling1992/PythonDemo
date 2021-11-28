# -*- coding: utf-8 -*-
import  os #导入文件操作
import datetime  # 导入日期时间库
import requests  # 导入http客户端库

"""
1.requests http 客户端请求库怎么用？
以百度：http://www.baidu.com为例
url = "http://www.baidu.com"
# 定义请求，请求结果赋值响应对象
# method：请求方法
# url：请求地址
response = requests.request(method="GET", url=url)
print(response)  # 打印响应对象
print(dir(response))  # 响应对象可以调用的属性和方法
# response.text # 响应的内容
print(response.text)
# response.encoding # 响应的字符集
print(response.encoding)
# response.headers # 响应的头信息
print(response.headers)
# response.status_code # 响应的状态码
print(response.status_code)
# response.cookies # 响应的会话信息
print(response.cookies)

# 怎么把响应内容里面的乱码转化为正常字符
response.encoding = "utf-8"
print(response.text)
"""

class SpiderSingle(object):
    # 定义一个初始化方法
    # 1.urls地址生成器，2.保存到html目录
    def __init__(self, urls, path):
        self.urls = urls
        self.path = path

    # 打印日志方法
    def log(self, url, save_path):
        # %Y：年，%m：月，%d：日，%H：时，%M：分，%S：秒
        print("{dt}:{url}->{save_path}".format(
            dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            url=url,
            save_path=save_path
        ))

    # 单线程爬取页面逻辑
    def catch_pages(self):
        # 1.定义请求生成器
        resps = (
            requests.request(method="GET", url=url) for url in self.urls
        )
        # 2.判断目录是否存在，并创建
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        # 请求迭代生成器，把响应的内容保存到html的文件中，再把html保存到相应的目录中
        n = 1
        for resp in resps:
            resp.encoding = "utf-8"
            save_path = os.path.join(
                self.path,
                "{}.html".format(n)
            )
            with open(save_path,"w",encoding="utf-8") as f:
                f.write(resp.text)
            n += 1
            self.log(resp.url, save_path)








