# 错误和异常

def div(x, y):
    z = x / y
    return z


#
# print(div(3, 4))
# print(div(3, 0))  #ZeroDivisionError: division by zero
# print(div(6, 6))  # 不能运行

# 使用try ...except
"""
语法格式：
try:
    正常代码块
except Exception as e:
    处理异常代码块
"""


def div1(x, y):
    try:
        z = x / y
        return z
    except  Exception as e:  # except  ZeroDivisionError as e:
        print("除法不能出现被0除的现象")
        print(e)  # division by zero


print(div1(3, 4))
print(div1(3, 0))
print(div1(6, 6))
