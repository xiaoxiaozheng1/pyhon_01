# 模块： 导入 ：有两种导入方式

# 1. 全部导入 import 模块的名字
import demo14_funcgaijin  # 导入的时候名字是demo14_funcgaijin文件名而不是__name__,在同一文件的时候名字是。

print(demo14_funcgaijin.add(3, 5))  # 不希望导入  print(add(6, 4))  print(add1(6, 4.3)) 使用__main__

# # 导入其他包下的模块
# from work.work1 import space
#
# print(space)
#
# # 模块的导入有两种全部导入和其他包下的导入
#
# import demo14_func
#
# demo14_func.add(3, 4)
#
# from work.work1 import space
#
# print(space)
