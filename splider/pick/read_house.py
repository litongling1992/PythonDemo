import pandas as pd
import pymysql
import hashlib
# 加上字符集参数，防止中文乱码
db_connection = pymysql.connect(
    host="127.0.0.1",
    database="spider",
    user="root",
    password="root",
    port=3306,
    charset='utf8'
)
# sql语句
sql_cmd = "select * from house;"
# 利用pandas 模块导入mysql数据
a = pd.read_sql(sql_cmd, db_connection)
# 创建md5对象
md = hashlib.md5()
house_datas = []
# 遍历DataFrame的每一行
for index, row in a.iterrows():
    address = (row['address'])
    # md5加密address
    md.update(address.encode(encoding='utf-8'))
    address_md = md.hexdigest()
    # 构建data数据
    data = [row['house_id'], row['provider_id'], address_md, row['address2'], row['ceng'], row['area'], row['paytype'],
            row['Status'], row['score'], row['Price']]
    create_time = row['Createtime'].strftime('%Y-%m-%d')
    data.append(create_time)
    update_time = row['Updatetime'].strftime('%Y-%m-%d')
    data.append(update_time)
    house_datas.append(data)
# 根据加密后的数据，重新构成DataFrame
df = pd.DataFrame(house_datas, columns=['house_id', 'provider_id', 'address', 'address2', 'ceng', 'area', 'paytype', 'Status',
                                  'score', 'Price', 'Createtime', 'Updatetime'])
df.to_csv("D:\Python\datas\house.csv", index=False, encoding="utf_8_sig")
