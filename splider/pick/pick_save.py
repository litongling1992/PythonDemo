# -*- coding: utf-8 -*-
import os
from lxml import etree  # 节点树库
import time  # 导入时间库
import datetime  # 导入日期时间库

"""
               # print(selector)

                # 获取细胞选择器 div下id=content的标签下的ul -> li -> div
                # 定义细胞选择器
                items = selector.xpath('//div[@id="content"]/ul/li/div')
                #for item in items:
                     #print(item)
            #         data.append(
            #             dict(
            #                 title=str(item.xpath('div[2]/div[1]/a/text()')[0]),
            #                 logo=str(item.xpath('div[1]/a[1]/img/@src')[0]),
            #                 url=str(item.xpath('div[1]/a[1]/@href')[0]),
            #                 preview=str(item.xpath('div[1]/a[2]/@href')[0]),
            #                 cate=str(item.xpath('div[2]/div[1]/ul/li/a/text()')[0]),
            #                 price=float(item.xpath('div[2]/div[2]/p/span/text()')[0])
            #             )
            #         )
        #return data
"""


class PickSave:
    # 定义初始化构造方法
    def __init__(self, path):
        self.path = path

    def pick(self):
        # 1.获取目录下的所有html文件
        html_list = os.listdir(self.path)
        # print(html_list)
        # 保存的数据
        data = []
        # 拼接html路径
        for html in html_list:
            html_path = os.path.join(self.path, html)
            #print(html_fullpath)
            # 打开html
            with open(html_path, "r", encoding="utf-8") as f:
                print(html_path)
                selector = etree.HTML(f.read())
                # 定义细胞选择器
                items = selector.xpath('//div[@id="primary"]/main/ul/li')
                #print(items)
                for item in items:
                    data.append(
                        dict(
                            title=str(item.xpath('div[2]/div[1]/a/text()')[0]),
                            logo=str(item.xpath('div[1]/a[1]/img/@src')[0]),
                            url=str(item.xpath('div[1]/a[1]/@href')[0]),
                            preview=str(item.xpath('div[1]/a[2]/@href')[0]),
                            cate=str(item.xpath('div[2]/div[1]/ul/li/a/text()')[0]),
                            price=float(item.xpath('div[2]/div[2]/p/span/text()')[0])
                        )
                    )
        return data



    @property
    def dt(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
