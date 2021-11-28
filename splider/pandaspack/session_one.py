# 实战一 项目
import pandas as pd
import os

# 获取父路径
cur_path = os.path.abspath(os.path.dirname(__file__))
# 获取myProject，也就是项目的根路径
root_path = cur_path[:cur_path.find("splider\\")+len("splider\\")]
# 获取olympics.csv文件的路径
data_path = os.path.abspath(root_path + 'data\\olympics.csv')
print(data_path)
if os.path.exists(data_path):
    # 读取数据,过滤掉前面4行
    oo = pd.read_csv(data_path, skiprows=4)

    # 1、In which events Jesse Owens win a medal
    jo = oo[oo.Athlete == "OWENS, Jesse"]
    # print(jo)
    # print(jo.Event.value_counts())

    # 2、找出羽毛球 男 金牌
    gold = oo[(oo.Medal == "Gold") & (oo.Gender == 'Men') & (oo.Sport == 'Badminton')]
    # print(gold)
    # 再根据年份排序
    gbm = gold.sort_values(by='Edition')
    # print(gbm)

    # 3、找出哪三个国家 在1984 - 2008年 获得奖牌最多
    rec = oo[(oo.Edition >= 1984) & (oo.Edition <= 2008)]
    noc = rec.NOC.value_counts().head(3)
    # print(noc)

    # 4、找出在男子100米 获得金牌的
    mge = oo[(oo.Medal == "Gold") & (oo.Gender == 'Men') & (oo.Event == '100m')]
    # print(mge)
    # 在按照年份降序 并列出指定项
    a_sort = mge.sort_values('Edition', ascending=False)[['City', 'Edition', 'Athlete', 'NOC']]
    print(a_sort)



