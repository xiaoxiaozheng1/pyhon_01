# os 模块
import os

os.listdir()
print(os.listdir())  # 返回当前路径下的所有文件和文件夹

print(os.getcwd())  # 返回当前的工作目录

print(os.path.exists("D:\project\pyhon_01"))  # 判断当前路径是否存在
print(os.path.exists("D:\project\pyhon_02"))

# datetime 模块
import datetime

print(datetime.datetime.now())

# sys 模块

import sys

print(sys.path)

# import os
#
# print(os.listdir())  # 返回当前路径下的所有文件和文件夹
# print(os.getcwd())  # 返回当前的工作目录
# print(os.path.exists("D:\project\pyhon_01"))
# print(os.path.exists("D:\project\pyhon_02"))
#
# # datetime 模块
# import datetime
#
# print(datetime.datetime.now())
#
# # sys 模块
# import sys  # 返回模块的搜索路径
#
# print(sys.path)
