# -*- coding: utf-8 -*-
import datetime
import os

from lxml import etree  # 节点树库
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.models import BsThemeProduct


class PickTest:
    # 定义初始化构造方法
    def __init__(self, path):
        self.path = path
        self.mysql_configs = dict(
            db_host="127.0.0.1",
            db_port=3306,
            db_user="root",
            db_pwd="root",
            auth_plugin="mysql_native_password",
            db_name="spider_data"
        )
        self.db = self.session

    # 定义连接会话
    @property
    def session(self):
        # 创建连接引擎
        engine = create_engine(
            "mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}".format(
                **self.mysql_configs
            ),
            encoding="utf-8",
            echo=True,
            pool_size=100,
            pool_recycle=10,
            connect_args={'charset': 'utf8'}
        )  # pool_size：连接池大小；pool_recycle：连接池生命周期；connect_args：连接选项
        # 定义会话
        Session = sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=True,
            expire_on_commit=False
        )  # bind绑定连接引擎；autocommit：True自动提交，False事务提交；autoflush：True自动刷新权限，False不自动；expire_on_commit：True自动提交，False事务提交
        return Session()

    def pick(self):
        # 获取所有html文件列表
        html_list = os.listdir(self.path)
        # 打印html的文件列表
        # print(html_list)

        # 保存的数据
        data = []
        for html in html_list:
            # 拼接单个html的文件全路径
            html_path = os.path.join(self.path, html)
            # print(html_path)

            # 打开html文件，并读取里边的内容
            with open(html_path, "r", encoding="utf-8") as f:
                # 得到读取的html文件的所有内容
                read_content = f.read()
                # print(read_content)

                # 定义一个选择器 转化为节点数据
                selector = etree.HTML(read_content)
                # print(selector)

                # 定义细胞选择器
                items = selector.xpath('//div[@id="content"]/ul/li/div')
                # print(items)

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

    def saveData(self):
        # 事务处理的逻辑
        try:
            # 执行代码块
            # 获取数据
            datas = self.pick()
            for v in datas:
                cd = dict(
                    createdAt=self.dt,
                    updatedAt=self.dt,
                    **v
                )
                bs_theme_product = BsThemeProduct(
                    **cd
                )
                # print(ba_theme_product)
                self.db.add(bs_theme_product)  # 添加数据至数据库中
        except Exception as e:
            print(e)
            # 如果出现异常，则回滚
            self.db.rollback()
        else:
            # 没有出现异常代码块
            self.db.commit()  # 提交
        finally:
            # 无论异常都得关闭
            self.db.close()  # 关闭会话
