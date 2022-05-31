# 需求 ： 要求：可以输入任何个数进行相加

# 可变化参数 ：参数的个数是可以运行变化的额，它有两种形式，分别是列表形式和字典形式

# 1.定义列表形式
def add(x, y, *args):
    print(args)
    z = x + y + sum(args)
    return z


print(add(3, 4))
print(add(3, 4, 5))
print(add(3, 4, 5, 6, 7, 8))
print(add(3, 4, 5, 6, 7, 8))
# 适用列表的方式进行传递调用
print(add(3, 4, 5, *[6, 7, 8]))
print(add(3, 4, 5, *(6, 7, 8)))


# print(add(3, 4, *(5, 6, 7, 8)))  # 传递列表


# 2.可变化参数-字典形式的参数
def show_info(**kwargs):
    print(kwargs)
    # return None


# 这里不写return就是默认有个return None
print(show_info(a='hello', b='world'))  # 传递位置参数
print(show_info(a='hello', b='world', c=123))
print(show_info(**{'key1': '你好呀！', 'key2': '很困呀！'}))  # 传递字典参数
