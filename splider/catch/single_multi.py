# -*- coding: utf-8 -*-

import time  # 导入时间库
import datetime  # 导入日期时间库
from multiprocessing.dummy import Pool
from multiprocessing import cpu_count

"""
1.对比单进程与多进程执行时间
"""


# 定义一个返回日期时间的函数
def dt():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# 运行函数
def run(v):
    print("{}:[{}]开始运行!".format(dt(), str(v).zfill(2)))
    time.sleep(2)
    print("{}:[{}]运行结束!".format(dt(), str(v).zfill(2)))


# 单进程的串行方式
def single():
    for i in range(0, 16):
        run(i)


# 多进程方式
def multi():
    # 判断核心数
    # 根据核心数量来开启多进程
    # 以进程池的方式运行函数
    n = cpu_count()

    # 创建进程池
    p = Pool(n)
    for i in range(0, 16):
        p.apply_async(run, args=(i,))  # 以进程池的方式运行函数，第一个参数为函数名，第二个参数是以元组的方式进行参数传递
    p.close()  # 关闭进程池
    p.join()  # 等待线程结束


# 如果程序结构等于自己
if __name__ == "__main__":
    start_time = time.time()
    # single()
    multi()
    print("总共用时:{}s".format(time.time() - start_time))