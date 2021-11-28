# -*- coding: utf-8 -*-
import os
import requests
from catch.spider_single import SpiderSingle
from multiprocessing.dummy import Pool
from multiprocessing import cpu_count


class SpiderMulti(SpiderSingle):
    # 执行请求方法
    def catch_page_process(self, url, filename):
        # 定义请求响应对象
        resp = requests.request(method="GET", url=url)
        # 判断保存的目录
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        # 保存并抓取响应内容
        resp.encoding = "utf-8"
        save_path = os.path.join(self.path, "{}.html".format(filename))
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(resp.text)
        # 输出抓取日志
        self.log(resp.url, save_path)

    # 多进程抓取方法
    def catch_pages(self):
        cpu_number = cpu_count()  # 获取CPU数量
        p = Pool(cpu_number)  # 定义进程池
        n = 1
        for url in self.urls:
            filename = str(n)
            p.apply_async(self.catch_page_process, args=(url, filename))
            n += 1
        p.close()
        p.join()
