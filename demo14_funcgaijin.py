# 函数 ： 具有特定的代码块，比如说登录功能，相加
"""
def 函数名字（参数列表）:
    代码块
"""


# 函数的定义：加法
def add(x, y):
    z = x + y
    return z


def add1(x, y):
    z = x + y
    return z

print(__name__)
# print(add(6, 4))
# print(add1(6, 4.3))
# return x+10,y

# 函数的调用

if __name__ == '__main__':

    print(add(6, 4))
    print(add1(6, 4.3))
