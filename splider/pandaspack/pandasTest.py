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
    csv_read = pd.read_csv(data_path, skiprows=4)
    # 显示数据前10条
    # print(csv_read.head(10))

    # 倒数2行
    # print(csv_read.tail(2))

    # 显示某一行
    # print(csv_read.iloc[0])

    # 显示某一列
    # print(csv_read['Edition'])
    # 显示某几列
    # print(csv_read[['Edition', 'Medal']])

    # 词频统计 将少的排在前面 则加参数ascending = True
    # print(csv_read.Gender.value_counts())

    # 排序操作 sort_values
    # ath = csv_read.Athlete.sort_values()
    # print(ath)
    # 先按照 Edition 排序 在按照 Athlete
    # ath = csv_read.sort_values(by=["Edition","Athlete"])
    # print(ath)

    # 查找金牌的
    # print(csv_read[csv_read.Medal == "Gold"])

    # 查找女运动员金牌的
    # print(csv_read[(csv_read.Medal == "Gold") & (csv_read.Gender == 'Women')])

    # 字符串的模糊查询 查找名字包含 Florence 的
    ath = csv_read.Athlete.str.contains("Florence")
    csv_read.str.c
    print(csv_read[ath])


